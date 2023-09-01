"""
hasattr , getattr, setattr, delattr
uses in OOP
"""
class Person:
    name = "Mahdi"
    age = 21

p1 = Person()

print(hasattr(p1, "name")) # you can send a class and obj.

print(getattr(Person, "age")) # send a value of attribute.

setattr(p1, "city", "Tehran") # add new attribute
print(getattr(p1, "city"))

delattr(p1, "city") # remove
print(getattr(p1, "city")) # AttributeError.