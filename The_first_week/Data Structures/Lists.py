# Lists are used to stored multiple values in a single variable.
# Apart of lists, there are also three of data types : Set, Dictionary, Tupel.
# Lists are created using ["example","example2",.....] or use the list()
# Lists items oredered(order will not change and the new items will be placed at the end of the list.) , changable(we can change, add, and remove items) ,
# and allow duplicate values.
# The first item has index [0] and the second [1].
# List items can be of any data type(int or string or boolean).
# We use lists insted of Arrays in python.(but if you want to actual arrays, you must import Numpy library)


### LIST is a collection which is ordered and changable. Duplicate values are ok.
### TUPLE is a collection which is ordered and unchagable. Duplicate values are ok.
### SET is a collection which is unordered and unchangable(add and remove is ok), unindexed. No Duplicate values.
### DICTIONARY is a collection which is ordered(python 3.6 and earlier unordered), changable. No Duplicate values.

thisislist= list(('a', 'b', 'c', 'd', 'e'))
print(thisislist[2:4]) # that the item in position 5 is NOT included
print(thisislist[-4:-1]) # the items from index -4 (included) to index -1 (excluded)

thisislists2 = ["apple", "banana", "cherry"] 

thisislists2[1:2] = ["blackcurrant", "watermelon"] 
print(thisislists2) # The length of the list will change when the number of items inserted does not match the number of items replace.

thisislists2.insert(2,"insert fruit") # As a result of the example above, the list will now contain 4 items.
print(thisislists2) 

thisislists2.append("append fruit")
print(thisislists2) 

thisislist.extend(thisislists2) # connect and append elements from another list to the current list.(you can add any itreable object such as tuples or sets...)
print(thisislist)

thisislists2.remove("cherry") # or thisislist2.pop(1) if you write pop() , the last element is removed.
print(thisislists2) 
del thisislists2[1] # thisislist2.clear() show to us [], but del thisislist2 delete list and error is back   
print(thisislists2)
print("#################################")
# loop lists
i = 0
while i < len(thisislists2):
    print(thisislists2[i])
    i += 1
print("################################")
for j in range(len(thisislists2)):
               print(thisislists2[j])
# [print(x) for x in thisislists2]

print("################################")
### LIST COMPREHENSION
thisislists3 = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in thisislists3:
#     if "a" in x: 
#            newlist.append(x)
newlist = [x for x in thisislists3 if "a" in x] # newlist = [expression for item in iterable if condition is true]
print(newlist) 
newlist = [x.upper() for x in newlist]
print(newlist)
newlist = ['replace to all' for x in thisislists3]
print(newlist)
newlist = [x if x != "banana" else "orange" for x in thisislists3] # return the item if it is not 'banana',if it is banana return 'orange'.
print(newlist)
print("################################")

thisislists3.sort(reverse=True) # sort descending
print(thisislists3)

print("################################")
def my_function(n):
        return abs( n -7) # calculate closet number to 50 and sortings ascending

thisislists4=[100,150,50,32,85]
thisislists4.sort(key = my_function) # sort by my function
print(thisislists4)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
