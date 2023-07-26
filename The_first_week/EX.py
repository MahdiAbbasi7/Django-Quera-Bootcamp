# Exception Handling 

# The try block lets you test a block of code for errors.
# The except block lets you handel the error.
# The else block lets you excute code when there is no error.
# The finally block lets you execute code, regardless of the result of try-and except blocks.

# try = test code
# except = handle error
# else = excute code if no error
# finally = execute code regardless of try-except

""" 
Python will normally stop and generate an error message but,
Error and exception can be handeled by try-except 

"""

try:
    print (x)
except:
    print ("An Exception occurred")
print ("###################################")
# Since the try block raises an error, the except block will be executed.

# Many exceptions
try :
    print(y)
except NameError:
    print("Exception")
except :
    print("An Exception occurred")

"""
SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
NameError: This exception is raised when a variable or function name is not found in the current scope.
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module.

"""

print ("###################################")
# ElSE
try: 
    print("no errors found in try block ,so @ else block @ is running ")
except:
    print("Exception is occured ")
else:
    print("this line for else block")

print ("###################################")
# FINALLY
#The finally block gets executed no matter if the try block raises any errors or not:
try:
  print(i)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Raise an exception
# To throw (or raise) an exception, use the raise keyword.
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")