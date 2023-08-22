a =(1,3)
b = "hello world"
c = []
d = 4

# LBYL -> "look before you leep"

# def check_method(obj):
#     if "__len__" in dir(obj): 
#         # we can use hasattr here (hasattr does check this attribute in obj or not)
#         # hasattr(obj,"__len__")
#         print(len(obj))
#     else:
#         print("No method defined")
# check_method(c)
# check_method(d)

# EAFP  -> "it's easier to ask for forgivness than permissions"
def check_method(obj):
    try:
        print(len(obj))
    except:
        raise Exception("No method defined")
check_method(c)
check_method(d)