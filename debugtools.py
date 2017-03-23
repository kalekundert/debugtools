#!/usr/bin/env python3

from __future__ import print_function
import inspect
from inform import indent, Color, render
from pathlib import Path
from types import ModuleType, FunctionType
import sys

__version__ = '0.3.9'

def p(*args, **kwargs):
    frame_depth = 1
    _print(frame_depth, args, kwargs)

def pp(*args, **kwargs):
    args = [
        render(arg) for arg in args
    ] + [
        '{k} = {v}'.format(k=k, v=render(v))
        for k, v in sorted(kwargs.items())
    ]
    frame_depth = 1
    _print(frame_depth, args, kwargs={'sep':'\n'})

def pv(*args):
    frame_depth = 1
    frame = inspect.stack()[frame_depth][0]
    variables = [(k, frame.f_locals[k]) for k in sorted(frame.f_locals)]
    args = [
        '{k} = {v}'.format(k=k, v=render(v))
        for k, v in variables
        if not k.startswith('_')
        if not isinstance(v, (FunctionType, type, ModuleType))
        if not args or v in args
    ]
    _print(frame_depth, args, kwargs={'sep':'\n'})


def _print(frame_depth, args, kwargs):
    frame = inspect.stack()[frame_depth + 1][0]

    try:
        # If the calling frame is inside a class (deduced based on the presence 
        # of a 'self' variable), name the logger after that class.  Otherwise 
        # if the calling frame is inside a function, name the logger after that 
        # function.  Otherwise name it after the module of the calling scope.

        self = frame.f_locals.get('self')
        frame_info = inspect.getframeinfo(frame)
        function = frame_info.function
        filename = frame_info.filename
        lineno = frame_info.lineno
        module = frame.f_globals['__name__']

        fname = Path(filename).name

        if self is not None:
            name = '.'.join([
                    self.__class__.__module__,
                    self.__class__.__name__,
                    function,
            ]) + '()'

        elif function != '<module>':
            name = '.'.join([module, function]) + '()'

        else:
            name = module

        highlight_header = Color('magenta', enable=Color.isTTY(sys.stdout))
        highlight_body = Color('blue', enable=Color.isTTY(sys.stdout))

        header = 'DEBUG: {fname}:{lineno}, {name}'.format(
            filename=filename, fname=fname, lineno=lineno, name=name
        )
        body = kwargs.get('sep', ' ').join(str(arg) for arg in args)
        header += ':\n' if body else '.'
        message = highlight_header(header) + highlight_body(indent(body))
        print(message, **kwargs)

    finally:
        # Failing to explicitly delete the frame can lead to long-lived 
        # reference cycles.
        del frame
