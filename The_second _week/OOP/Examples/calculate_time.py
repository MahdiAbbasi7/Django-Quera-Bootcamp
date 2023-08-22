from time import perf_counter
from functools import wraps

def time_calculations(func):
    @wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start_time = perf_counter()
        value =func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print("The run time of :",func.__name__, "is: " ,run_time )
        return value
    return wrapper_decorator
@time_calculations
def my_func():
    print("This is your time for run function")
my_func()