# Abstract base class
from abc import ABC, abstractmethod

class Empoly(ABC):
    @abstractmethod
    def calculate_salary(self):
        """This method is must be implemented"""

class HourlyEmployee(Empoly):
    def calculate_salary(self, hour):
        self.hour = hour * 60
        print(f"Calculating Hourly Employee : {self.hour}")
class SalariedEmployee(Empoly):
    def calculate_salary(self, hour):
        self.hour = hour * 65
        print(f"Calculating Hourly Employee : {self.hour}")
    
test = HourlyEmployee()
test.calculate_salary(20)
test = SalariedEmployee()
test.calculate_salary(20)
print(40 * "-")
# ----------------------------------------------------------------

class Car(ABC):
    @abstractmethod
    def start(self):
        """This method is must be implemented"""
        print("Starting....")
    @abstractmethod
    def stop(self):
        """This method is must be implemented"""
        print("Stopping....")
    
class SportsCar(Car):

    def start(self, brand:str):
        super().start()
        print(f"Brand is : {brand}")

    def stop(self, brand:str):
        super().stop()
        print(f"Brand is : {brand}")

test2 = SportsCar()
test2.start("benz")
test2.stop("benz")
print(40 * "-")
# ----------------------------------------------------------------

class Person(ABC):
    @abstractmethod
    def greet(self):
        print("Hello")
    @abstractmethod
    def introduce(self):
        print("Introducing")

class Student(Person):
    def greet(self):
        super().greet()
        print("Student greeting")
    def introduce(self):
        super().introduce()
        print("Teacher greeting")
        
    def name(self,name, age, position):
        print(f"Student name : {name}, age : {age} ,  and is: {position}")

class Teacher(Person):
    def greet(self):
        super().greet()
        print("Student greeting")
    def introduce(self):
        super().introduce()
        print("Teacher greeting")
    def name(self,name, age, position):
        print(f"Teacher name : {name} , age : {age},  and is: {position}")

test3 = Student()
test3.greet()
test3.introduce()
test3.name("mahdi",21,"Student")
print(40 * "-")
test4 = Teacher()
test4.greet()
test4.introduce()
test3.name("ehsan",41,"Teacher")

