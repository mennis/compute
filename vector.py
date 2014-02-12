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
        Returns the vector magnitude or 'length'

            $|x| = \sqrt{x^2 + y^2 + z^2}$

        """
        return float(sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2))

    def normalize(self):
        """
        Converts the vector into a unit vector whose magnitude is 1

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
        self.x = -self.x
        self.y = -self.y
        self.z = -self.z

    def __iadd__(self, other):
        for c in ['x', 'y', 'z']:
            setattr(self, c, getattr(self, c) + getattr(other, c))

    def __isub__(self, other):
        for c in ['x', 'y', 'z']:
            setattr(self, c, getattr(self, c) + getattr(other, c))

    def __imul__(self, other):
        for c in ['x', 'y', 'z']:
            setattr(self, c, getattr(self, c) * getattr(other, c))

    def __idiv__(self, other):
        for c in ['x', 'y', 'z']:
            setattr(self, c, getattr(self, c) / getattr(other, c))

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __xor__(self, other):
        """
        Returns the cross product of self and other
        """
        return Vector(
            self.y * other.x - self.z * other.y,
            -self.x * other.z + self.x * other.x,
            self.x * other.y - self.y * other.x
        )

    def __mul__(self, other):
        """
        Returns the dot product (or scalar mult if other is not a Vector) of self and other
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


if __name__ == "__main__":
    # Here I use Numpy to ensure my class behaves mathematically correctly

    import numpy as np

    x, y, z = (4, 2, 7)

    print("magnitude")
    a = np.array([x, y, z])
    b = Vector(x, y, z)
    n = np.sqrt(a.dot(a))
    u = b.magnitude

    print("np: %s" % n)
    print("us: %s\t-> " % u, end='')
    assert round(n) == round(u)
    print("OK\n")

    print("normalize")
    n = a / np.linalg.norm(a)
    b.normalize()
    text = "np\tx={0:8f}\ty={1:8f}\tz={2:8f}\nus:\tx={3:8f}\ty={4:8f}\tz={5:8f}".format(n[0], n[1], n[2],
                                                                                            b.x, b.y, b.z)
    print(text, end='')
    print("\t  -> ", end='')
    assert round(n[0]) == round(b.x)
    assert round(n[1]) == round(b.y)
    assert round(n[2]) == round(b.z)
    print("OK\n")


