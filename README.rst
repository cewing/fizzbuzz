********
FizzBuzz
********

A pair of simple example functions that implement the fizzbuzz game.

``fizzbuzz``
============

For any given 'n', print 'Fizz' if n is divisible by 3, 'Buzz' if n is
divisible by 5, and 'FizzBuzz' if in is divisible by *both* 3 and 5. For all
other numbers, print that number.

.. code-block:: pycon


    >>> from fizzbuzz import fizzbuzz
    >>> for i in range(16):
    ...     print fizzbuzz(i)
    ...
    0
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz


``fizzbuzz_extended``
=====================

Implement the FizzBuzz game, but allow arbitrary extensions.  For example,
numbers divisible by seven should print as 'Sezz'.

.. code-block:: pycon

    >>> from fizzbuzz import fizzbuzz_extended
    >>> extras = {7: 'Sezz'}
    >>> for i in range(16):
    ...     print fizzbuzz_extended(i, extras)
    ...
    0
    1
    2
    Fizz
    4
    Buzz
    Fizz
    Sezz
    8
    Fizz
    Buzz
    11
    Fizz
    13
    Sezz
    FizzBuzz


.. image:: https://api.travis-ci.org/cewing/simple-echo-server.png
    :alt: Travis CI Tests
