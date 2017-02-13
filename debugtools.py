#!/usr/bin/env python3

__version__ = '0.0.0'

from pprint import pprint
pp = pprint

def p(message=None):
    import inspect
    frame = inspect.stack()[1][0]
        
    try:
        # Collect all the variables in the scope of the calling code, so they 
        # can be substituted into the message.

        scope = {}
        scope.update(frame.f_globals)
        scope.update(frame.f_locals)

        # If the calling frame is inside a class (deduced based on the presence 
        # of a 'self' variable), name the logger after that class.  Otherwise 
        # if the calling frame is inside a function, name the logger after that 
        # function.  Otherwise name it after the module of the calling scope.

        self = frame.f_locals.get('self')
        function = inspect.getframeinfo(frame).function
        module = frame.f_globals['__name__']

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

        if message is not None:
            print(name + ': ' + str(message).format(**scope))
        else:
            print(name)

    finally:
        del frame


def v():
    """
    pprint all variables in calling scope
    """
    import builtins
    pprint(builtins.vars())

