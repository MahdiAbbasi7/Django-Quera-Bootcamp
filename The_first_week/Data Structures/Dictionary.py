# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered(As of Python version 3.7), changeable and NO duplicates.
# Dictionary written by {} and have keys and values.
# Can be referred to by using the key name.
dictionary = {
    "name": "Mahdi",
    "last_name": "Abbasi",    
    "age": 21,
    "age": 22,
    "man": True,
    "benefit":["python", "Django", "Databases", "DRF", "...."]
}

print(dictionary)
print(len(dictionary))

# Order will not change and when your write a duplicate item, value is updated to last value. ===> age == 22 not 21
# The values in dictionary items can be of any data type.(int, float, string, boolean)
# The constructor of dictionary is  dict(). example: dictionary1 = dict(name = "John", age = 36, country = "Norway")
# Not two (())
print ("###############################")

### Accessing in dict
# We can use get() insted ["key"] 
print(dictionary.get("name"))
# We can use keys() to access to all keys in dictionary.
print(dictionary.keys()) # we can track changes of keys in dictionary. 
# We can use values() to access all values in dictionary.
print(dictionary.values()) # we can track changes of values in dictionary
# We can use items() to access all items in dictionary.
# print(dictionary.items()) # we can track changes of items in dictionary

# For checking if key exists use in keyword.(just keys)
print ("###############################")
# You can change and add new items in dictionary by update() and change like : thisisdict[key] = newvalue (use = no :)
dictionary.update({"name": "Mohammad Mahdi"})
print(dictionary)

print ("###############################")
# For remove items we can use pop() and popitem() . pop give a key and remove key but popitem() removes last inserted item.( before python 3.7, a random item)
dictionary.pop("man")
# dictionary.popitem()
print(dictionary)

# The del keyword can also delete the dictionary completely and raise an error.
# The clear() method empties the dictionary and not raise an error.
print ("###############################")
# You can loop through a dictionary by using a for loop.
for x in dictionary:
    print(dictionary[x]) # this line returns all values..
    # print(x) # this line returns all keys.
# or you can use this code
for y in dictionary.items(): #dictionary.keys() or dictionary.values()
    print(y) 

print ("###############################")

### copy dictionary
# Make a copy of a dictionary with the copy() method.
# And another way is use dict()
copyofdict = dict(dictionary)
print(copyofdict)

print ("###############################")

### nested dictionary
# Create a dictionary that contain another dictionaries

myfamily =  {
    "child_1" : {
        "name": "Mahsa",
        "age": 35
    },

    "child_2" : {
        "name": "Narges",
        "age": 35
    },

    "child_3" : {
        "name": "Mahdi",
        "age": 35
    },

    "child_4" : {
        "name": "Hafez",
        "age": 7
    }
}
print(myfamily["child_3"]["name"])
# also you can use this syntax 
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }


# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	    Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	    Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary