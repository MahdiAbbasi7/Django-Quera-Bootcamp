"""
Multi-threading in pyhton.
use passing a callable object to the constructor.
"""
from time import perf_counter, sleep
from threading import Thread

start = perf_counter()

def show(name):
    print (f"Starting {name}")
    sleep(3)
    print(f"Fininshing {name}")

"""
target is name of callable object (without paranthesis)
args is a list or tuple of arguments for the target invocation.
"""
t1 = Thread(target = show, args= ("one",))
t2 = Thread(target = show, args= ("two",))

"""
This functions for start the thread's activity 
It must be called at most once per thread object.
"""
t1.start()
t2.start()

"""
Wait until the thread terminates.
"""
t1.join()
t2.join()

end = perf_counter()

print(f"Time of  this code : {round(end - start)} seconds")

