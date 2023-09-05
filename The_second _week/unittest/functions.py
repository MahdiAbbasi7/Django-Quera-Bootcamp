"""
Before this file, check extra directories.
"""

from itertools import islice
from functools import partial
from collections.abc import Sequence
from collections import deque

l = ["A","B","C","D","E"]
m = []

_marker = object()

def slice(iterabel, number):
    return list(islice(iterabel, number))

def chancked_func(iterabel, number, strict = False):
    iterator = iter(partial(slice, iter(iterabel), number), [])
    # strict = if iterabel % number == 0 return false
    if strict :
        if number is None:
            raise ValueError("number must be a positive number and not none or negative.")
        def ret():
            for chanck in iterator:
                if len(chanck) != number:
                    raise ValueError("iterator is not devided by number.")
                yield chanck
        return iter(ret())
    else:    
        return iterator

def first(iterable, default=_marker):
    # if default is None, raise exception
    try:
        return next(iter(iterable))
    except StopIteration as e:
        if default is  _marker:
            raise ValueError("first was called on an empty, and no  default"
                             "value was provided.") from e
        return default

def last(iterable, default=_marker):
    try:
        if isinstance(iterable, Sequence):
            return iterable[-1]
        elif hasattr(iterable, "__reversed__"):
            return next(reversed(iterable))
        else:
            return deque(iterable, maxlen=1)[-1]
    except (IndexError, TypeError, StopIteration):
        if default is _marker: 
            raise ValueError("default must be provided.")
        return default

def nth_or_last(iterable, n, default=_marker):
    return last(islice(iterable, n+1), default=default) # n+1 becuase we use index.

def one(iterable, too_short =None, too_long=None):
    it = iter(iterable)
    try:
        first_value = next(it)
    except StopIteration as e:
        raise(
            too_short or ValueError('too few items in iterable (expected 1)')
        ) from e
    
    try:
        second_value = next(it)
    except StopIteration:
        pass
    else:
        msg = (
            'Expected exactly one itme in iterable, but got {!r}, {!r}, '
            'and perhaps more.'.format(first_value, second_value)
        )
        raise too_long or ValueError(msg)
    return first_value





# print(nth_or_last([],0, "ali"))
# print(last(m, 4))
# print(first(l))
# print(first(m))
# print(slice(l, 2))
# print(list(chancked(l,3, strict=True)))