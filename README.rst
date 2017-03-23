``debugtools`` --- Easily print useful debugging information
============================================================

version = 0.3.9

.. image:: https://img.shields.io/pypi/v/debugtools.svg
   :target: https://pypi.python.org/pypi/debugtools

.. image:: https://img.shields.io/pypi/pyversions/debugtools.svg
   :target: https://pypi.python.org/pypi/debugtools

.. image:: https://img.shields.io/travis/kalekundert/debugtools.svg
   :target: https://travis-ci.org/kalekundert/debugtools

.. image:: https://img.shields.io/coveralls/kalekundert/debugtools.svg
   :target: https://coveralls.io/github/kalekundert/debugtools?branch=master

This package provides a handful of functions you can use to print debugging 
information.  There are basically two things that are useful about these 
functions.  First, they're only one or two letters each, so you can type them 
really quickly while debugging.  Second, they append the name of the calling 
function to whatever you're printing, so you can easily see where each message 
came from (and you don't have to hunt down print statements once you finish 
debugging).

Installation
============
You can install ``debugtools`` using ``pip``::

   $ pip install debugtools

Usage
=====
I typically add the following import to the beginning of any file that I'm 
likely to debug:

.. code:: python

   >>> from debugtools import p, pp, pv

The ``p()`` function behaves just like ``print()``, except it appends the name 
and location of the calling context to whatever you're printing and indents and 
colors the output.  I often use it with no arguments, just to see if a function 
is being called or not.

.. code:: python

    >>> a = 1
    >>> b = 'this is a test'
    >>> c = (2, 3)
    >>> d = {'a': a, 'b': b, 'c': c}
    >>> p(a, b, c, d)
    DEBUG: <doctest README.rst[5]>:1, __main__:
        1 this is a test (2, 3) {'a': 1, 'b': 'this is a test', 'c': (2, 3)}

The ``pp()`` function pretty prints its arguments, one per line.

.. code:: python

    >>> pp(a, b, c, d)
    DEBUG: <doctest README.rst[6]>:1, __main__:
        1
        'this is a test'
        (2, 3)
        {
            'a': 1,
            'b': 'this is a test',
            'c': (2, 3),
        }

If you pass in keyword arguments, the name of the argument is prepended to its 
value.

.. code:: python

    >>> pp(a=a, b=b, c=c, d=d)
    DEBUG: <doctest README.rst[7]>:1, __main__:
        a = 1
        b = 'this is a test'
        c = (2, 3)
        d = {
            'a': 1,
            'b': 'this is a test',
            'c': (2, 3),
        }

The ``pv()`` function calls ``pp()`` with the dictionary of variables from the 
calling scope, so it's a good way to see what variables are defined in the 
function you're debugging.

.. code:: python

    >>> pv()
    DEBUG: <doctest README.rst[8]>:1, __main__:
        a = 1
        b = 'this is a test'
        c = (2, 3)
        d = {
            'a': 1,
            'b': 'this is a test',
            'c': (2, 3),
        }

You can optionally specify specific variables to ``pv()``, and only those 
variables are printed.

.. code:: python

    >>> pv(b, d)
    DEBUG: <doctest README.rst[9]>:1, __main__:
        b = 'this is a test'
        d = {
            'a': 1,
            'b': 'this is a test',
            'c': (2, 3),
        }

This last feature is not completely robust. The checking is done by value, so if 
several variables share the value of one requested, they are all shown.

.. code:: python

    >>> aa = 1
    >>> pv(a)
    DEBUG: <doctest README.rst[11]>:1, __main__:
        a = 1
        aa = 1
