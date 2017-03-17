``debugtools`` --- Easily print useful debugging information
============================================================
This package provides a handful of functions you can use to print debugging 
information.  There are basically two things that are useful about these 
functions.  First, they're only one or two letters each, so you can type them 
really quickly while debugging.  Second, they append the name of the calling 
function to whatever you're printing, so you can easily see where each message 
came from (and you don't have to hunt down print statements once you finish 
debugging).

.. image:: https://img.shields.io/pypi/v/debugtools.svg
   :target: https://pypi.python.org/pypi/debugtools

.. image:: https://img.shields.io/pypi/pyversions/debugtools.svg
   :target: https://pypi.python.org/pypi/debugtools

.. image:: https://img.shields.io/travis/kalekundert/debugtools.svg
   :target: https://travis-ci.org/kalekundert/debugtools

.. image:: https://img.shields.io/coveralls/kalekundert/debugtools.svg
   :target: https://coveralls.io/github/kalekundert/debugtools?branch=master

Installation
============
You can install ``debugtools`` using ``pip``::

   $ pip install debugtools

Usage
=====
I typically the following import at the beginning of any file that I'm likely 
to debug:

.. code:: python

   from debugtools import p, pp, pv

The ``p()`` function behaves just like ``print()``, except it appends the name 
and location of the calling function to whatever you're printing.  I often use 
it with no arguments, just to see if a function is being called or not.

The ``pp()`` function pretty prints its arguments, one per line. If you pass in 
keyword arguments, the name of the argument is prepended to its value.

The ``pv()`` function calls ``pp()`` with the dictionary of variables in the 
calling scope, so it's a good way to see what variables are defined in the 
function you're debugging.

