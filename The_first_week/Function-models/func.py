# A function is a block of code that which only runs when it is called.
# We can pass data as arguments to the function and a function can return data as result.

### Calling Functions'
# we can call functions by <name_of_funct>()
def firstfunc():
    print ("Hello this is first func")

firstfunc()
### Arguments or args
# we can pass arguments to functions when you want send some data to func(sperate arguments by comma ",")
def secondfunc(firsparamets, secondparameters):
    print (firsparamets + " and " + secondparameters)

secondfunc("this is first argument", "this is second argument") # pass values of arguments when you call function.

### Parameters vs Arguments
# A parameter is the VARIABLE listed inside the parentheses in the function definition. ==> firstparameter
# An argument is the VALUE that is sent to the function when it is called. ==> "this is first argument"

### Arbitrary Arguments
# By default, a function must be called with the correct number of arguments.
# If you do not know how many arguments passed into your function, add a * before the parameter name in the function.
def multipleparameters(*my_favorites,test):
    print("Mahdi are interested in " + my_favorites[0] + test)
# tuple of arguments,
multipleparameters("Software Engineering","Python", test= " and Django",) # in test we pass to func by Keyword Arguments.

### Arbitrary Keyword Arguments
# Use **kwargs before
def multiplekwargs(**children):
    print ("My children name is " + children["child_3"]) 

multiplekwargs(child_1="Mahsa",child_2="Narges",child_3="Mahdi",child_4="Hafez")

### If you want set default values call the function without argument and set default value in parametrs.

# Pass a list as args
def listargs(listargs):
    for x in listargs:
        print(x) 
listone = list(("apple","kiwi","banana"))
listargs(listone)

### Recursion
# . It means that a function calls itself.you can loop through data to reach a result.
print("################################")
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
