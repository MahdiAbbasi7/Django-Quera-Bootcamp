"""
abc = abstract base classes
this module checks one class has some attributes or not.
"""
from collections.abc import Sequence, Container, Sized

# for Sequence
def one(args):
    if isinstance(args, Sequence):
        print("Yes, args is a sequence from abc")
    else:
        print("No, is not a sequence from abc")

one({})

# ------------------------------contains----------------------------------
l = [1, 2, 3, 4, 5]
if 1 in l:
    print (True) 

class one:

    def __str__(self) -> str:
        pass

    # for Container
    def __contains__(self, item):
        pass
    
    # for Sized
    def __len__(self) -> int:
        return 1

a = one()
print(isinstance(a, Container)) # False, after creating __contains__ method returns True.
print(isinstance(a, Sized))