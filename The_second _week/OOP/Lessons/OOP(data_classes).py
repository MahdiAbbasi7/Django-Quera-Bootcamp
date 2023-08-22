"""
This module provides a decorator and functions for adding generated "special methods",
Like __init__ and __repr__
If you want to add your initial values use ClassVar or InitVar.
"""
from dataclasses import dataclass

@dataclass
class Person:
    """Initializes a new Person object"""
    # if in parameters write forzen = True, you can override fields and initialize(below of another fileds) , age : int = 19 
    firstname: str
    lastname: str
    age: int
    # data hint in dataclasses is necessary.
    def __post_init__(self):
        if self.age <= 0:
            raise ValueError("Age must be greater than zero....")

    def return_values(self):
        return [self.firstname, self.lastname, self.age]

@dataclass
class Person2(Person):
    gender : str
    
    def return_values(self):
        super().return_values()
        return [self.firstname, self.lastname, self.age, self.gender]


p = Person("Mahdi", "Abbasi", 21)
p2 = Person2("John", "Bin", 81,"man")
print(p.return_values())
print(p2.return_values())