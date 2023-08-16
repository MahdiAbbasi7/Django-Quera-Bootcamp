# Everything in python is an object.
# Every object is at least one instance of a class(built-in).
# A variable is a reference to an object.
# Each class is an object of the type class and all classes inherit from a class named object.
# In the new structure of Python, the concept of class is considered equal to the concept of type.

# print(x.__class__) is equivalent print(type(x))
from __future__ import annotations # for some changes is updated version of python
from math import hypot
import datetime
# first,second= 6,5

# print(type(first * second))
# print(id(first))

# print("#########objects############")

# class Point():
#     pass 
# print(Point.__class__)
# print(Point.__bases__)

# i = Point() # instanciation from the class
# j = Point() # instanciation  from the class

# i.x = 5 # add attribute for i
# i.y = 4 # add attribute for i
# j.x:int = 3 # add attribute for j (should be integer)

# print("#########function and methods############")
# # methods have a self and inside a class but functions have't self
# class Methods:
#     def methods(self):
#         self.ones = "ones"
#         self.two = "two"

# instance = Methods()

# instance.methods() # call methods
# # or 
# # Methods.methods(instance) # call methods
# print(instance.ones)
# print(instance.two)



print("#########example############")
class Example:
    def __init__(self, x: float = 0, y: float=0)->None:
        self.x= x
        self.y= y
        # No return in this function

    def move(self,x:float,y:float)-> None: # None is type of output
        self.x= x
        self.y= y

    def reset(self):
        self.move(0,0)
    
    def distance(self, other:"Example")-> float:
        return hypot(self.x-other.x, self.y-other.y)

p1 = Example()
print(p1.x, p1.y)

p2 = Example()
print(p2.x, p2.y)

# p1.reset()
# print(p1.x, p1.y)

# p2.move(3,4)
# print(p2.x, p2.y)

# # distance between p1 and p2
# print(p1.distance(p2))

#----------------------------------------------------------------

# Constructor in python : 
# __new__ for create
# __init__ for initialization (special methods for dander(__))
p3 = Example(0,0) # you must pass a value for initialization and defult values.
print(p3.x, p3.y)
# print(help(hypot))

#----------------------------------------------------------------
# underscore for accessibility in python (public , private, protected)
# in python we don't have actual accessibility , and you can use private classes and methods with some way.
print("#########underscore############")
# use just underscore
for _ in range(5):
    print("using underscore")

nametest, _, _ = ("mahdi", 21, 4)
print (nametest)
print(_)

# and use in python terminals to fine the last command that runs.


# use underscore before name of variables or methods
# public = no any underscore
# protected = _name
# private = __name --> name mangling (add name of class befor name of methods and variables)

class User:
    def __init__(self, name="", phone=""):
        self.__user_id = id(self)
        self._name = name
        self.phone = phone

class Account(User):
    def __init__(self):
        super().__init__()
        self.__user_id = "1234"

     
mahdi =  User("Mahdi", "902")
mahdi_account = Account()

print(mahdi._User__user_id) # access to the private variables --> "_nameofclass__privatevariable"
print(mahdi._name)
print(mahdi.phone)
print(mahdi_account._Account__user_id)

# use underscore after name of variables or methods
# for variables that similar to built-in functions.
max_ = [3, 4, 5, 6, 7, 8, 9]
print(max(max_))


"""
use dander(__) after and befor name of variables or methods
for special methods like __getattr__
"""

print("#########seter and geter############")
class Uni:
    def __init__(self, teacher="", student=""):
        self.__teacher = teacher
        self.student = student
    def set_teacher(self, teacher): # control attributes
        if len(teacher) <= 15 :
            self.__teacher = teacher
        else :
            raise ValueError("Teacher must be ltr 15 characters")
        
    def get_teacher(self): #return attribute
        return self.__teacher

test = Uni()
test.set_teacher("firoz nadery")
prof = test.get_teacher()
print(prof)


#----------------------------------------------------------------
print("#########str and repr############")

# str -> strring -> __str__(usually for user )
# reper -> repersentions -> __rep__ (usually for developer and debuging purposes)
today = datetime.datetime.now()
print(str(today)) # defualt of print is a string so we don't need str().
print(repr(today))
print(datetime.datetime(2023, 8, 1, 19, 39, 40, 518209)) # create again object 


# __reper is defualt in puthon so we must create a __str__ method and customize it.
class Person():
    def __init__(self, firstname, lastname, age) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def __str__(self):
        return f'{self.firstname},{self.lastname},{self.age}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.firstname}', '{self.lastname}',{self.age})"
        
    

user = Person("mahdi","abbasi", 22)
print(user)
print(repr(user)) #or print(user.__repr__()) 


#----------------------------------------------------------------
print("#########Instance attribute and class attribute############")

user2 = Person("John", "Sina", 35)
print(user2.firstname) #instance attribute


# in class attribute we don't use "self" and outside of we create this attribute(global)
