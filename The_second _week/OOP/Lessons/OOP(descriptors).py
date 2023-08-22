"""
Descriptors are classes that override getter/setter/del methods.
Create some methods for my attributes.

"""
# Descriptor class
class NameField:
    # def __init__(self,name=None):
    #     self.name = name
    # uses set name
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner): # instance is a object and owner returns creator of class
        # print(instance) # <__main__.Person object at 0x0000029578364CD0>
        # print(owner) # <class '__main__.Person'>
        return instance.__dict__[self.name] 
    
    def __set__(self,instance, value):
        if 0 < len(value) < 15:
            # self.name = value this line store in object of NameField class
            instance.__dict__[self.name] = value # store in object of Parent class (p)
        else : 
            raise ValueError("Value must be between 1 and 15 characters.", len(value))

    def __delete__(self,instance):
        print("deleting")
        del instance.__dict__[self.name] 

class Person:
    Childname = NameField() # this is  change to attr no obj.
    Fathername = NameField() 
    Mothername = NameField()

    def __init__(self,Child,Father,Mother):
        self.Childname = Child
        self.Fathername = Father
        self.Mothername = Mother


p = Person("Mahdi","Ali","Leyla")
print(p.Childname)
print(p.Fathername)
print(p.Mothername)
print(p.__dict__)