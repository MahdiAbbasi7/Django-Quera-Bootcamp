from threading import Thread, Event
from time import sleep


def first(f,s):
    print("First is ready...")
    f.set() # first is ready
    s.wait() # wait for second thread
    print("First is working...")
    s.clear() 
    print("First is finishing...")

def second(f,s):
    sleep(10)
    print("second is ready...")
    s.set() # second is ready
    f.wait() # wait for first thread
    print("second is working...")
    f.clear() # 
    print("second is finishing...")

f = Event()
s = Event() # if we are use Event, we don't need join()

t1 = Thread(target=first, args=(f,s))
t2 = Thread(target=second, args=(f,s))

t1.start()
t2.start()

# First is ready...
# second is ready...
# second is working...
# First is working...
# second is finishing...
# First is finishing...