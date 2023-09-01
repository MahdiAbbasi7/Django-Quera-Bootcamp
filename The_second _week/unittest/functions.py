"""
Before this file, check extra directories.
"""

from itertools import islice
from functools import partial

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
    


# print(first(l))
# print(first(m))
# print(slice(l, 2))
# print(list(chancked(l,3, strict=True)))