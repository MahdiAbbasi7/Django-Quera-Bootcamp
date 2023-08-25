"""
Multi-threading in pyhton.
use overriding the run () method in a subclass.
"""
from threading import Thread 
from time import sleep, perf_counter


start = perf_counter()

def show(name, delay):
    print (f"Starting {name}")
    sleep(delay)
    print(f"Fininshing {name}")


class ShowThread(Thread):
    def __init__(self, name, delay:int) :
        """Overrides Constructor """
        super().__init__() # this line should be written
        self.name = name
        self.delay = delay

    def run(self):
        """Method representing the thread’s activity."""
        show(self.name, self.delay)
    
t1 = ShowThread("one", 3)
t2 = ShowThread("two", 5)

t1.start()
t2.start()

t1.join()
t2.join()


end = perf_counter()

print(f"Time of  this code : {round(end - start)} seconds")

# Starting one
# Starting two
# Fininshing one
# Fininshing two
# Time of  this code : 5 seconds