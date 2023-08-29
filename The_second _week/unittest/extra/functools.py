"""
Functool ==> 1.partial && 2.update_wrapper
"""

from functools import partial, update_wrapper

def multi(x,y):
    """for doc"""
    return x*y


double = partial(multi, y=4) # or x = 4 (defualt is x)
print(double(4))

update_wrapper(double, multi)

print(double.__name__)
print(double.__doc__)