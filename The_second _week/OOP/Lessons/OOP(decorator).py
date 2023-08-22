"""
how we can use decorators in classes??
"""

# decorators implamations by classes and functions
from functools import wraps


class MyClassDecorator:
    # implement init and call
    def __init__(self, clas):
        self.clas = clas
    def __call__(self):
        print("Do something befor function.")
        return self.clas()

@MyClassDecorator
class MyTest:
    def __init__(self):
        self.num = 5
    
obj = MyTest()
print(obj.num)









# wrapper usese for docstrings and functionality decorators

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Do something befor function.
        print("Do something befor function.")
        func(*args, **kwargs)
        # Do something after function.
        print("Do something after function.")


    return wrapper # without parantes

@my_decorator
def myfunc():
    """Example docstring for function myfunc"""
    print("MAHDI")
# myfunc()