"""
Simplest class in multi-threading library
"""

from threading import Thread, Timer

def show():
    print("this is an example")

t = Timer(5, show)
t.start()
# t.cancel()
