"""
count method in itertools module.
"""

from itertools import count

# n = count(start = 0, step =2)
# # print(next(n))

# ################################

# for i in count(0,1):
#     # print(i)
#     pass

################################
names = ['Mahdi', 'Nika', 'mahsa']

for i in zip(count(1, 1), names): # zip(numbers, list) -> add numberst before list.
    print(list(i))

################################
n =map(lambda x: x **2, count(1, 1))

for i in n:
    if i > 100:
        break
    print(i)
    