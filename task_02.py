#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """ Object returns birthday year and informs upong invalid year.
    Attributes:
        None
    """
    pass


def get_age(birthyear):
    """Returns the birth year if valid.
    Arguments:
        age (int): Age of user.

    Returns:
        age (int): Birthyear of user.

    Examples:
    >>> get_age(2099)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        __main__.InvalidAgeError
    >>> get_age(30)
        1985
    """
    age = datetime.datetime.now().year - birthyear
    if age > 0:
        return age
    else:
        raise InvalidAgeError
