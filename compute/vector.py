# -*- coding: utf-8 -*-

from __future__ import print_function
from math import sqrt


class Vector(object):
    """
    A pure python vector class.
    """

    def __init__(self, x=float(0), y=float(0), z=float(0), tolerance=0.0001):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.tolerance = tolerance

    @property
    def magnitude(self):
        """
        return the vector magnitude or 'length'

            $|x| = \sqrt{x^2 + y^2 + z^2}$

        """
        return float(sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))

    def normalize(self):
        """
        converts the vector into a unit vector whose magnitude is 1

            $|x| = \sqrt{x^2 + y^2 + z^2} = 1$

        """
        m = self.magnitude
        if m <= self.tolerance:
            m = 1
        self.x /= m
        self.y /= m
        self.z /= m

        for c in ['x', 'y', 'z']:
            component = getattr(self, c)
            if abs(component) < self.tolerance:
                setattr(self, c, 0.0)

    def reverse(self):
        """
        reverse the vector by applying the negative of each component x, y, z
        """
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z

    def __iadd__(self, other):
        for c in ['x', 'y', 'z']:
            setattr(self, c, getattr(self, c) + getattr(other, c))
        return self

    def __isub__(self, other):
        for c in ['x', 'y', 'z']:
            setattr(self, c, getattr(self, c) - getattr(other, c))
        return self

    def __imul__(self, other):
        for c in ['x', 'y', 'z']:
            setattr(self, c, getattr(self, c) * getattr(other, c))
        return self

    def __idiv__(self, other):
        for c in ['x', 'y', 'z']:
            setattr(self, c, getattr(self, c) / getattr(other, c))
        return self

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __xor__(self, other):
        """
        return the cross product of self and other
        """
        return Vector(
            self.y * other.x - self.z * other.y,
            -self.x * other.z + self.x * other.x,
            self.x * other.y - self.y * other.x
        )

    def __mul__(self, other):
        """
        return the dot product (or scalar mult if other is not a Vector) of self and other
        """
        if type(other) is not Vector:
            return Vector(self.x * other + self.y * other + self.z * other)
        else:
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)

    def __repr__(self):
        r = str()
        for c in ['x', 'y', 'z']:
            r += "%s = %s\n" % (c, getattr(self, c))
        return r
