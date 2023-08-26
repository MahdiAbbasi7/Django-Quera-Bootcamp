"""
Introduction to current-thread and enumrate methods
"""
from time import sleep, perf_counter
from threading import Thread, current_thread, enumerate

start = perf_counter()

def show(name):
    print(f"Starting {name}")
    print(current_thread()) # for number use current_thread().ident
    print(enumerate())
    sleep(3)
    print(f"Finishing {name}")

t1 = Thread(target=show, args=("one",), name="First thread") # for rename = current_thread()
t2 = Thread(target=show, args=("two",), name="Second thread")

t1.start()
t2.start()

t1.join()
t2.join()

end = perf_counter()

print(f"Time of  this code : {round(end - start)} seconds")

# Starting one
# <Thread(First thread, started 11672)>
# Starting two
# [<_MainThread(MainThread, started 18936)>, <Thread(First thread, started 11672)>, <Thread(Second thread, started 18308)>]
# <Thread(Second thread, started 18308)>
# [<_MainThread(MainThread, started 18936)>, <Thread(First thread, started 11672)>, <Thread(Second thread, started 18308)>]
# Time of  this code : 3 seconds