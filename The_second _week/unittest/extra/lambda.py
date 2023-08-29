"""
Lambda functions.
lambda (args): manipulation(args)
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("numbers:", nums)
"""Even and odd numbers."""
even = filter(lambda x: x%2 ==0, nums)
odd = filter(lambda x: x%2 == 1, nums)
print("even nums: ", list(even) ,"\nodd nums: ", list(odd))

"""The filter function is used to filter some specific elements from a sequence."""
filter_numbers = filter(lambda x: x>6 , nums)
print("filter :", list(filter_numbers))

"""The map function is used to apply a specific operation to each element in a sequence."""
squared_result = map(lambda x: x*x, nums) 
print("multi numbers:", list(squared_result))

"""The sorted function is used to sort the elements by your optional keys."""
elements = [(0,'z'),(4,'a'),(8,'s'),(3,'b'),(2,'o')]
sorted_result = sorted(elements, key= lambda x: x[1]) # sort by alphabet
print(sorted_result)

