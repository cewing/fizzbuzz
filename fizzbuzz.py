#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The module provides two functions, fizzbuzz and fizzbuzz_extended
"""


data = ((3, 'Fizz'), (5, 'Buzz'))


def fizzbuzz(n):
    """return a fizzbuzz-formatted representation of n"""
    if n == 0:
        return str(0)
    out = ''
    for divisor, replacement in data:
        if not n % divisor:
            out += replacement
    if not out:
        out = str(n)
    return out
