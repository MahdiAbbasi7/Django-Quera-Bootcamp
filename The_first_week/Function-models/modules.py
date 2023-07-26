# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application
# Save your module as a python file (.py) and using import statements where you want to use them.
# You can create an alias when you import a module, by using the as keyword
# use the syntax: module_name.function_name.


import func

func.secondfunc("test from another module", "test from another module2")


# you are access to variables 
for x in func.listone:
    print(x)

print("##################################")
### Bulit-in modules 
# Platform
import  platform
print (platform.uname()) 

# dir()
# list all the function names (or variable names) in a module
# can be used on all modules, also the ones you create yourself.
#  Printing all variables and function from module
import sys
# print (dir(sys))


from func import listargs
argstest = list (("test from func", "test from func2", "test from func3"))
listargs(argstest)

""" 
Note: When importing using the from keyword, 
do not use the module name when referring to elements in the module.
Example: person1["age"], not mymodule.person1["age"]

"""
