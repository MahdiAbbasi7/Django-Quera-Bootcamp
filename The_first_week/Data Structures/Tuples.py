# Tuples are used to store multiple values to a single variable.
# A tuple is a collection which is orederd but UNCHANGEABLE.(or immutable )
# Written tuples by ("example",....,)
# The first element has index [0] and the second element [1].....
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Tuples items can be any data type.(int, float, string, bool)
# Constractor of tuples are : tupel() ==> test = tuple(("mahdi",22,True))
# Index of items in tuples is accessed by <name of tuple>[i]

test = ("apple",) # This is one tuple
test1 = ("apple") # but is not . SO REMEMBER COMMA AFTER THE ITEMS

thisistuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango") 
print(thisistuple[3:6]) # start at 3 (included) and end at index 6(not included)
print(thisistuple[-4:-1]) # start at -1 (not included) and end at index -4 (included)

### workhands for handel unchangeable
# 1 - convert tuple to list and change , and return as a tuple.
listoftuple = list(thisistuple) # remember () not []
listoftuple[0] = "tuple to list"
thisistuple = tuple(listoftuple)
print(thisistuple)

# 2 - add tuple to a tuple
y = ("another way",)
thisistuple += y #
print (thisistuple) 

# We can use the above methods to remove items and "del thisistuple" delete the tuple completly and raise an error.

# assign the values to the tuples calling "packing" , also we have "unpacking"
print("################################")
fruits = ("apple", "banana", "cherry", )
(blue, green, yellow) = fruits # we assign a colors to fruits

print(blue)
print(green)
print(yellow)
print("################################")
# also you can use Asterisk * to unpack if  the number of variables is less than the number of values
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(blue, green, *yellow, red) = fruits # Python will assign values to the variable until the number of values left matches the number of variables left.
print(blue)
print(green)
print(yellow)
print(red)

# Loops in tuples such as  in Lists (for and while)

# Joins in Tuples
print("################################")

# we can use + to join two or more tuples

tuple1 =("hassan", "ali", "toomaj")
tuple2 =(1, 2, 3)
join = tuple1 + tuple2
print(join)
# you can use * to multiply the content of a tuple a given number of times

multiplytuple = tuple1 * 3
print(multiplytuple)


# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found