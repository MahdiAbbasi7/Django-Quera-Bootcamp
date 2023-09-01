"""
Double ended queue
deque method, from collections and containers datatypes.
deque => list-like container with fast appends and pops on either end.
in project uses for add new jobs to the queue and delete old jobs.
"""
from collections import deque

l = [1,2,3,4]

l.append(5) # add the end of list. [1,2,3,4,5]
l.pop() # remove the end of list. [1,2,3,4]

d = deque("mahdi") # send iterable (like string not numbers)
print(d)
d.append("abbasi") # add the right of list.
print (d)
d.appendleft("mohammad")
print(d)
d.extendleft([2])
print(d)