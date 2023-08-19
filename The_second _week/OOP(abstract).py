"""
Abstract base class is usefull for implementing a class that has general topics.
You can't create an object from Abstract classes (Just concreate classes. )
2 methods for implementation:
    1- inheritance
    2- you can use ABCMeta
"""
from abc import ABC , abstractmethod

# Abstract base class
class Vehicle(ABC):

    @abstractmethod
    def move(self):
        """this method should be implemented"""
        print("this is Default and use super function.")
    @abstractmethod
    def repair(self):
        """this method should be implemented"""

# Other abstract base classes  
class LandVehicle(Vehicle):
    @abstractmethod
    def breaking(self):
        """this method should be implemented"""
    
class AirVehicle(Vehicle):
    @abstractmethod
    def eject(self):
        """this method should be implemented"""
        

# Concrete classes
class Car(LandVehicle):
    def move(self):
        super(Car, self).move() # Access to Defult and abstract methods in Vehicle.
        print("Moving Car...")
    def repair(self):
        print("Repairing Car...")
    def breaking(self):
        print("Breaking Car...")
class Airplane(AirVehicle):
    def move(self):
        print("Flying Airplane...")
    def repair(self):
        print("Repairing Airplane...")
    def eject(self):
        print("Ejecting Car...")
    
test =  Car()
test.move()
test.repair()
test.breaking()
print("\n))))))))))))))))))))))))\n")
test2 = Airplane()
test2.move()
test2.repair()
test2.eject()







"""
NOTE: You can use multi decorators for your functions:
    @classmethod
    @abstractmethod
    def func(cls):
        pass
"""