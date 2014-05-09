# -*- coding: utf-8 -*-
"""
Basic numerical tools for use where numpy, et. al. are unavailable.
"""

from __future__ import print_function
import math
import functools


def filter_for(function):
    """
    A decorator for slicing data from a list of dicitonaries.
    If the wrapped function is called with::

        field=<some key>

    extract data from a list of dicts if field is specified
    given a structure like::

        [{'bw': 2029.6, 'io': 458152.0, 'iops': 16236.0, 'runt': 226039.0},
        {'bw': 2046.8, 'io': 458252.0, 'iops': 16374.0, 'runt': 224134.0},
        {'bw': 2019.5, 'io': 458352.0, 'iops': 16155.0, 'runt': 227173.0},
        {'bw': 2005.4, 'io': 458452.0, 'iops': 16042.0, 'runt': 228762.0}]

    and field='bw' this will present [2029.6, 2046.8, 2019.5, 2005.4] to
    the wrapped function
    """

    @functools.wraps(function)
    def wrapper(values, field=None):
        if field:
            v = list()
            for l in values:
                v.append(l.get(field))
        else:
            v = values
        return function(v)

    return wrapper

@filter_for
def getfrom(v):
    """
    pass through function for using the
    filter_for decorator directly
    """
    return v


@filter_for
def median(v):
    """
    :param v: a list of numerical values
    :return: statistical median for a list of values expressed as a float
    """
    v.sort()
    m = len(v) / 2

    if not len(v) % 2:  # not even
        return (v[m - 1] + v[m]) / 2.0  # average the middle two
    else:
        return v[m]


@filter_for
def average(v):
    """
    :param v: a list of numerical values
    :return:  average for a list of values expressed as a float
    """
    return sum(v) * 1.0 / len(v)


@filter_for
def variance(v):
    """
    :param v: a list of numerical values
    :return: the variance of a list of values expressed as a float
    """
    return average(map(lambda x: (x - average(v)) ** 2, v))


@filter_for
def standard_dev(v):
    """
    :param v: a list of numerical values
    :return: the variance of a list of values expressed as a float
    """
    return math.sqrt(variance(v))
