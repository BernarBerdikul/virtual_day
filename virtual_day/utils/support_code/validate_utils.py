from decorator import decorator
from collections import OrderedDict
import itertools
import inspect

"""
CODE from lib python 'validators',
link: https://github.com/kvesteri/validators/blob/master/validators/utils.py
This code base on 'Django' utils validator
Need to catch custom exception and return wrong message to front
"""


class ValidationFailure(Exception):
    def __init__(self, func, args):
        self.func = func
        self.__dict__.update(args)

    def __repr__(self):
        return u'ValidationFailure(func={func}, args={args})'.format(
            func=self.func.__name__,
            args=dict(
                [(k, v) for (k, v) in self.__dict__.items() if k != 'func']
            )
        )

    def __str__(self):
        return repr(self)

    def __unicode__(self):
        return repr(self)

    def __bool__(self):
        return False

    def __nonzero__(self):
        return False


def func_args_as_dict(func, args, kwargs):
    """
    Return given function's positional and key value arguments as an ordered
    dictionary.
    """
    _getargspec = inspect.getfullargspec

    arg_names = list(
        OrderedDict.fromkeys(
            itertools.chain(
                _getargspec(func)[0],
                kwargs.keys()
            )
        )
    )
    return OrderedDict(
        list(zip(arg_names, args)) +
        list(kwargs.items())
    )


def validator(func, *args, **kwargs):
    """
    A decorator that makes given function validator.
    Whenever the given function is called and returns ``False`` value
    this decorator returns :class:`ValidationFailure` object."""
    def wrapper(func, *args, **kwargs):
        value = func(*args, **kwargs)
        if not value:
            return ValidationFailure(
                func, func_args_as_dict(func, args, kwargs)
            )
        return True
    return decorator(wrapper, func)
