"""
# Basic of meta class in python 

Evryting in python is an object. and any class that implements is inhertenced from "object" and an instance from "type".
But Meta class in python is  a class of a class that defines how a class behaves. 
Meta class is a class from which the object is created.
"""
class HumanMeta(type):
    pass

class Human(metaclass=HumanMeta):
    pass
h=Human
print(type(h))
print(type(Human))
print(type(HumanMeta))
