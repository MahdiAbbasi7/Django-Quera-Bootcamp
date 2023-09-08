"""
Before this file, check extra directories.
"""

from itertools import islice, chain, repeat, tee, starmap
from functools import partial
from collections.abc import Sequence
from collections import deque
from time import monotonic
from operator import sub

l = ["A","B","C","D","E"]
m = [1, 2, 3]

_marker = object()

def raise_exception(exc, *args):
    raise exc(*args)

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

def interleave(*iterable):
    return chain.from_iterable(zip(*iterable))

def repeat_each(iterable, n = 2):
    return chain.from_iterable(map(repeat, iterable, repeat(n)))

def strictly(iterable, n , too_short=None, too_long=None):
    if too_short is None:
        too_short = lambda item_count: raise_exception(
            ValueError, 
            f'too few items in iterable (got {item_count})'
        )
    if too_long is None:
        too_long = lambda item_count: raise_exception(
            ValueError, 
            f'too many items in iterable (got at least {item_count})'
        )
    it = iter(iterable)
    for i in range(n):
        try:
            item = next(it)
        except StopIteration:
            too_short(i)
            return
        else :
            yield item
    try:
        next(it)
    except StopIteration:
        pass
    else:
        too_long(n+1)

def only(iterable, defualt=None,  too_long=None):
    it = iter(iterable)
    first_value = next(it, defualt) # if it is none , return defualt.

    try :
        second_value = next(it)
    except StopIteration:
        pass
    else:
        msg = (
            'Expected exactly one item in iterable but got {}, {}, and perhaps more.'.format(first_value, second_value)
        )
        raise too_long or ValueError(msg)
    return first_value

def always_reverse(iterable):
    try:
        return reversed(iterable)
    except TypeError: 
        return reversed(list(iterable))

def always_iterable(obj, base_type= (str, bytes)):
    if obj is None: return iter(())

    if (base_type is not None) and isinstance(obj, base_type):
        return iter(obj,)
    
    try:
        return iter(obj)
    except TypeError:
        return iter((obj,))
    
def split_after(iterable, pred, max_split = -1):
    if max_split == 0:
        yield list(iterable)
        return
    buf =[]
    it = iter(iterable)
    for item in it:
        buf.append(item)
        if pred(item) and buf:
            yield buf
            if max_split == 1:
                yield list(it)
                return
            buf = []
            max_split -= 1
    if buf:
        yield buf

def split_into(iterable, sizes):
    it = iter(iterable)
    for size in sizes:
        if size is None:
            yield (list(it))
            return
        else:
            yield list(islice(it, size))

def map_if(iterable, pred, func, func_else=lambda x: x):
    for item in iterable:
        yield func(item) if pred(item) else func_else(item)

class time_limited:
    def __init__(self, limite_seconds, iterable) -> None:
        if limite_seconds < 0 :
            raise ValueError ('limit seconds must by positive.')
        self.limite_seconds = limite_seconds
        self._itrable = iter(iterable)
        self._start_time = monotonic()
        self.timed_out = False

    def __iter__(self):
        return self
    
    def __next__(self):
        item = next(self._iterable)
        if monotonic() - self._start_time > self.limite_seconds:
            self.timed_out = True
            raise StopIteration
        return item

def difference(iterable, func=sub, *, initial=None): # * after python 3, and that means you must send keyword-arguments to function.
    a, b = tee(iterable) # copy two(a, b) iterables 
    try:
        first = list(next(b))
    except StopIteration:
        return iter([])
    
    if initial is not None:
        first = []
        return chain(first, starmap(func, zip(a, b))) # a+b by zip, send to func by starmap, result of starmap + first by chain.

def value_chain(*args):
    for value in args:
        if isinstance(value, (str, bytes)):
            yield value
            continue
        try:
            yield from value # nested is not valid
        except TypeError:
            yield value


# print(list(repeat_each(l)))
# print(list(interleave(l, m)))
# print(one(m))
# print(nth_or_last([],0, "ali"))
# print(last(m, 4))
# print(first(l))
# print(first(m))
# print(slice(l, 2))
# print(list(chancked(l,3, strict=True)))