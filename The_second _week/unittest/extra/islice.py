"""
This method is used for sliceing iterables itmes.
This method from itertools module.
"""
from itertools import islice


numbers = [1,2,3,4,5,6,7,8,9,10]
slice = islice(numbers, 5)
slice2 = islice(numbers, 0, None)
slice3 = islice(numbers, 0, None, 2 )

print(list(slice))
print(list(slice2))
print(list(slice3))