# Such as len() and print(), because this function can be used in multiple Datatypes
print("M" + "A")
print(2 + 2)
print(2 + 2j + 3 )

print(25 * "*" + "examples"+ 25 * "*" ,"\n" )

class Cat(object):
    def __init__(self, name:str , color:str):
        self.name = name
        self.color = color

    def info(self):
        print ( f"Hi, I'm {self.name} and my color {self.color}")

    def sound(self):
        print ("Meow......")
    
class Cow(object):
    def __init__(self, name:str , color:str):
        self.name = name
        self.color = color
    
    def info(self):
        print( f"Hi, I'm {self.name} and my color {self.color}")
    
    def sound(self):
        print ("Moo......")

def funk(obj):
    obj.info()
    obj.sound()
      
cat = Cat("cat", "yellow")
cow = Cow("cow", "white")

funk(cat)
funk(cow)
