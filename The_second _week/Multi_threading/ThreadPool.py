"""
Sometimes you are want to use a lot of threads in your project, but also for do this ,
you should be write many codes.
so use Thread pool.
"""
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def show(name):
    print (f"Starting {name}")
    sleep(3)
    print(f"Fininshing {name}")

with ThreadPoolExecutor() as executor:
    names = ["one", "two", "three", "four", "five", "six"]
    executor.map(show,names)

print("finished")

# Starting one
# Starting two
# Starting three
# Starting four
# Starting five
# Starting six
# Fininshing one
# Fininshing two
# Fininshing three
# Fininshing four
# Fininshing five
# Fininshing six
# finished