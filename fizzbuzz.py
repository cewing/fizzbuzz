#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The module provides two functions, fizzbuzz and fizzbuzz_extended
"""
from __future__ import print_function
import os
os


def fizzbuzz(n):
    """return a fizzbuzz-formatted representation of n"""
    if n == 0:
        return str(0)
    out = ''
    if not n % 3:
        out += 'Fizz'
    if not n % 5:
        out += 'Buzz'
    if not out:
        out = str(n)
    return out


def fizzbuzz_extended(n, additional={}):
    """return a fizzbuzz-formatted representation of n, with extensions

    If passed, the `additional` arg should be a dictionary keyed by integer
    with the values being the desired string substitution for that integer
    """
    if n == 0:
        return str(0)
    base = {3: 'Fizz', 5: 'Buzz'}
    base.update(additional)
    out = ''
    for x in sorted(base.iterkeys()):
        if not n % x:
            out += base[x]
    if not out:
        out = str(n)
    return out


if __name__ == '__main__':
    print("FizzBuzz Produces:")
    for i in xrange(100):
        print(fizzbuzz(i), end=" ")
    print()
    others = {7: 'Sizz', 11: 'Elzz'}
    for i in xrange(100):
        print(fizzbuzz_extended(i, others), end=" ")
    print()
