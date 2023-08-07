# class base(): # or write class base(object):
#     pass
# print(base.__base__) # All classes are inhertances of class object

# # for inheritance write name of class and in parantes write name of class that you want inheritance.
# # add search method to lists(overrides)
# class SearchList(list):
#     def search(self,number:str) -> bool:
#         # list_of_nambers: list[str] = []
#         for num in self:
#             if number in num :
#                 return True

print("#########super and override############")
# change methods of superclass in subclass
# super is a way to add methods of superclass to subclass. (super().__init__())
class first(object):
    def __init__(self):
        print(" first")
class second(object):
    def __init__(self):
        super().__init__()
        print(" second")
class third(object):
    def __init__(self):
        super().__init__()
        print(" third")
class fourth(object):
    def __init__(self):
        super().__init__()
        print(" fourth")

fourth() # first \n second \n third \n fourth

