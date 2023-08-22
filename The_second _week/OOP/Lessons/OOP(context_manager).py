"""
For writing same tasks that should be executed before or after the main task.
1- inter method
2- exit method

"""

class SameClass:
    
    def __enter__(self):
        print("Enter mehtod ,befor main task \n")
        return self

    def __exit__(self, exc_type, exc_value, exc): # this parameter is used for exception handling.
        print("Exit mehtod ,after main task \n")

# or write maintask = SameClass()
with SameClass() as maintask:
    print(maintask.__class__)
    print("this is your main task \n")

# 