"""
Race condition
Thread safe
Dead lock
Rlock
"""

from threading import Thread , Lock


number = 0 # shared recources
lock = Lock()

def add():
    global number
    with lock:
        for _ in range(1000):
            number += 1

def subtract():
    global number
    with lock : 
        for _ in range(1000):
            number -= 1

t1 = Thread(target=add)
t2 = Thread(target=subtract)

t1.start()
t2.start()

t1.join()
t2.join()

print(number)
print("done")

# maybe sometimes result is different and not 0. => race condition
"""
Rlock : acquired multiple times by the same thread.
"""