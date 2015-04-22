#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """Object looks for index in variable.
    Attributes:
        None
    """
    try:
        return var1[var2]
    except IndexError:
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
    except KeyError:
        print 'Warning: Your index/key doesn\'t exist.'
        return var1
