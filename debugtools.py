#!/usr/bin/env python3

import inspect
from inform import indent, output, Color, render
from pathlib import Path

__version__ = '0.3.3'

def p(*args, **kwargs):
    frame_depth = 1
    _print(frame_depth, args, kwargs)

def pp(*args, **kwargs):
    args = list(args) + [
        '{k} = {v}'.format(k=k, v=render(v))
        for k, v in kwargs.items()
    ]
    frame_depth = 1
    _print(frame_depth, args, kwargs={'sep':'\n'})

def pv(**kwargs):
    frame_depth = 1
    frame = inspect.stack()[frame_depth][0]
    args = [
        '{k} = {v}'.format(k=k, v=render(v))
        for k, v in frame.f_locals.items()
        if not k.startswith('_')
    ]
    _print(frame_depth, args, kwargs)


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

        highlight_header = Color('magenta')
        highlight_body = Color('blue')

        header = 'DEBUG: {fname}:{lineno}, {name}:'.format(
            filename=filename, fname=fname, lineno=lineno, name=name
        )
        body = kwargs.get('sep', ' ').join(str(arg) for arg in args)
        message = highlight_header(header) + '\n' + highlight_body(indent(body))
        output(message, **kwargs)

    finally:
        # Failing to explicitly delete the frame can lead to long-lived 
        # reference cycles.
        del frame
