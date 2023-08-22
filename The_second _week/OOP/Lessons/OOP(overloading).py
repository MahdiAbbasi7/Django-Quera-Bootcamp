"""

Binary Operators:
Operator	Magic Method
+	__add__(self, other)
-	__sub__(self, other)
"*	__mul__(self, other)"
/	__truediv__(self, other)
"//	__floordiv__(self, other)"
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)

"""



"""


Comparison Operators:
Operator	Magic Method
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
"!=	__ne__(self, other)"

"""
# for more information check this link : https://www.geeksforgeeks.org/operator-overloading-in-python/


class Persons:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # Oveload function
    def __eq__(self, gender: object) -> bool:
        return self.gender == gender
        

    def __str__(self):
        return f"{self.name}, {self.age},{self.gender}"
    
test = Persons("mahdi", 21, "man")
test2 = Persons("erfun", 21, "man")

print(test == test2) # use overloading

# ----------------------------Slots------------------------------------
# you can use __slots__ to accessibilities for your parameters and objects of classes
# slots are Tupels
class TestSlots:
    __slot__ =("a", "b") # just a and b (not c or ....)
    def __init__(self,a,b):
        self.a = a
        self.b = b
test = TestSlots(3,2)
print(test.a, test.b)