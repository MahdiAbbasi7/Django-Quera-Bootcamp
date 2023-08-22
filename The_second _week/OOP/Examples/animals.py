from pprint import pprint

class Animals(object) :
    """ Manage Base classes"""
    def __init__(self, name:str, spaces:str)->None:
        self.name = name
        self.spaces = spaces
    
    def make_sounds(self) -> str:
        return ("Generic animal sound")

class Mammal(Animals):
    """Create a subclass 1 """
    def __init__(self, legs:int, **kwargs)->None:
        super().__init__(**kwargs)
        self.legs = legs
    
    def make_sound(self)-> str:
        super().make_sounds()
        return ("Generic mammal sound")

class Dog(Mammal):
    """Create subclass2 """
    def __init__(self,category:str, **kwargs)->None:
        super().__init__(**kwargs)
        self.category = category
    
    def make_sounds(self)-> str:
        super().make_sounds()
        return ("Woof")

test = Dog(name="Jessy", spaces="Haski" , category="Dog", legs=4)
test.make_sounds()
pprint([test.name, test.category, test.legs, test.spaces] )