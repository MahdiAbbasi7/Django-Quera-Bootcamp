""" 
    We use getter and setter for improve security and accessibility, and for authentication.
    This methods have a disadvantage like is complex to write and read, and in big projects 
    We must edit many line to make sure . so we use Property

    Properties usefully override the methods that behavior like attributes
    (write func but use as attributes)

"""
class Color():
    def __init__(self, rgb, name):
        self._rgb = rgb
        if name :
            self._name = name
        else :
            raise ValueError("Invalid name") 

    @property 
    def name(self):
        """FIRST : getter function"""
        return self._name
    
    @name.setter
    def name(self, name):
        if name :
            self._name = name
        else :
            raise ValueError(f"Invalid name{name!r}")
    
    @property 
    def rgb(self):
        """SECOND : getter function"""
        return self._rgb
    
    @rgb.setter
    def rgb(self, rgb):
        self._rgb = rgb
    
    @name.deleter
    def name(self):
        del self._name
    
    # name = property(fget=_get_name, fset=_set_rgb, fdel=_del_name,doc="new doc")
    # or write : rgb = property(_get_rgb, _set_rgb) 
    
last_test = Color(0x2312 ,"optional")
last_test.name = "red"
print(last_test.name)
print(last_test.rgb)
# help(last_test)


# test =  Color(0x6783F5, "light blue")
# print(test._get_name())
# test._set_rgb(0x091B66)
# test._set_name("blue")
# print(test._get_rgb())

# print("*" * 40)

# test =  Color(0xED1F1F, "light red")
# print(test.name)
# test.rgb = 0xED1F1F
# test.name = "red"
# print(test.rgb)