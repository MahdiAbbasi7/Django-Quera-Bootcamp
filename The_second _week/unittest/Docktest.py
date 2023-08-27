"""doctest tutorial"""

import doctest

def add(a,b):
    """
    add function
    >>> add(5,3)
    8
    >>> add(-2,2)
    0
    """
    return a + b

def subtract(a,b):
    """
    subtract function
    >>> subtract(5,3)
    2
    >>> subtract(-2,2)
    -4
    """
    return a - b

def divide(a,b):
    """
    divide function
    >>> divide(6,3)
    2.0
    >>> divide(-2,2)
    -1.0
    """
    return a / b

def multiply(a,b):
    """
    multiply function
    >>> multiply(5,3)
    15
    >>> multiply(2,"t")
    'tt'
    """
    return a * b

# 4 items passed all tests:
#    2 tests in Docktest.add
#    2 tests in Docktest.divide
#    2 tests in Docktest.multiply
#    2 tests in Docktest.subtract
# 8 tests in 5 items.
# 8 passed and 0 failed.
# Test passed.