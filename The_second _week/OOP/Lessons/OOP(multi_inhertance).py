# Java is not supported this inhertance
from pprint import pprint
class SuperClass1(object):
    def __init__(self,p1) -> None:
        self.p1 = p1

class SuperClass2(object):
    def __init__(self,p2) -> None:
        self.p2 = p2

class SubClass(SuperClass1,SuperClass2): # Priority of SuperClass1 is higher than SuperClass2.
    def __init__(self,p1,p2,p3):
        # super(SuperClass1,self).__init__(p1) # this line super create a some ambiguity. we can handle this :
        SuperClass1.__init__(self,p1)
        SuperClass2.__init__(self,p2)
        self.p3 = p3

obj = SubClass(1,2,3)
print(obj.p1)
print(obj.p2)
print(obj.p3)
# ----------------------------------------------------------------
print(30 *  "#", "MRO(diamond-problem)", 30 *  "#",)
# MRO(method resolution orientated)

class BaseClass(object):
    num_base_classes = 0

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def call_me(self):
        print("Calling method on Baseclass")
        self.num_base_classes += 1

class LeftClass(BaseClass):
    num_left_classes = 0
    
    def __init__(self, c, **kwargs) -> None:
        super().__init__(**kwargs)
        self.c = c

    def call_me(self):
        # BaseClass.call_me(self) # replace super().call_me()
        super().call_me()
        print("Calling method on leftclass")
        self.num_left_classes += 1

class RightClass(BaseClass):
    num_right_classes = 0

    def __init__(self, d, e, **kwargs) -> None:
        super().__init__(**kwargs)
        self.d = d
        self.e = e

    def call_me(self):
        # BaseClass.call_me(self)
        super().call_me()
        print("Calling method on rightclass")
        self.num_right_classes += 1

class SubClass(LeftClass,RightClass):
    Sub = 0

    def __init__(self, f, **kwargs) -> None:
        super().__init__(**kwargs)
        self.f = f

    def call_me(self):
        # LeftClass.call_me(self)
        # RightClass.call_me(self)
        super().call_me()
        print("Calling method on Subclass")
        self.Sub += 1

test = SubClass(a=1, b=2, c=3, d=4, e=5, f=6)
test.call_me()
print("\n ##### Show order of MRO ##### \n")
pprint(SubClass.__mro__) # left, right, base, object
print("\n ##### initializing in multi ingertance (use **kwargs) ##### \n")
pprint([test.a, test.b, test.c, test.d, test.e, test.f])
