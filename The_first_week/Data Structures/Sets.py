# Sets are used to store multiple values in a single variable.
# A set is a collection which is unordered, unchangeable(add, remove is ok), and unindexed, No duplicate values(True and 1 is a same).
# Sets are written by {}
# Each time you run a set , oreder is changed.
# Set items can be of any data type(int, float, string, bool)
# Constractor of sets are : set() ==> test = set(("mahdi",22,True))
# You can't access itmes in a set by refrring to an index or a key, but you can use for loop
thisisset = {"Mahdi", "Abbasi", 21, True}
for x in thisisset:
    print (x) # remember the response is not ordered.
    # print("Mohammad" in thisisset) ===> False

### once a set is created, you can't change it itmes, but you can add new items.
# To add new item use add() method

thisisset.add("add new item by add()") # just one  argument
print(thisisset)

# Also you can use update() method to add new itme or multiple items
thisisset2 = {"Narges", "Abbasi", 23,1} # no duplicate and true and 1 is same so just add Narges and 23
thisisset.update(thisisset2)
print(thisisset)

# In update() method you can add any iterable

test = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

test.update(mylist)

print(test)

print("############################")


### To remove an item in a set, use the remove(), or the discard() method. 
# If the item to remove does't exist, remove() raise an error, but discard() NO and return set without any changes.
test.remove("apple")
print(test)
# discard not delete
test.discard("chery")
print(test)
# pop is removed a random item, so you cannot be sure what item that gets removed.
test.pop()
print(test)
# clear() method empties the set and returns set()
test.clear()
print(test)
# The del keyword will delete the set completely and raise an error.
# del test
# print (test)
print("############################")
###  You can loop through the set items by using a for loop
# for x in thisisset:
#     print(x)
print("############################")
### several ways to join two or more sets in Python.(union, update, intersection_update, intersection, symmetric_difference_update, symmetric_difference)
# for update method go to line 21
thisisset3 = set((1, 2, 3))
unionset = thisisset.union(thisisset3)
print(unionset) #  Both union() and update() will exclude any duplicate items.

# The intersection_update() method will keep only the items that are present in BOTH sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y) # if you use intersection() method, you must defentions a new variable becuase this method return a new set 
# z = x.intersection(y)
print(x)

# The symmetric_difference_update() method is NOT of intersection_update() and intersection().(items that are NOT present inBOTH sets.)
x.symmetric_difference_update(y)
# z= x.symmetric_difference(y)
print(x)

# Method	Description
# add()	    Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()  Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard() Remove the specified item
# intersection()    Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()     Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others