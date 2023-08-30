"""
Before this file, check extra directories.
"""

from itertools import islice
from functools import partial

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

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

# print(slice(l, 5))
# print(list(chancked(l,3, strict=True)))