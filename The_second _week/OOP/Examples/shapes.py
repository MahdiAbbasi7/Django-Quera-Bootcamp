from typing import Any


class Shape():
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.area = 0
        self.perimeter = 0

    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

    def show(self):
        info = ""
        for k, v in self.__dict__.items():
            if v > 0 :
                info += f"{k}: {v:.2f} \n"
        print(info)

    def __str__(self):
        return self.__class__.__name__
    
# length, width
class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.length + self.width)

# length
class Square(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def calculate_area(self):
        self.area = self.length ** 2

    def calculate_perimeter(self):
        self.perimeter = 4 * self.length
    
    def __call__(self, length) -> Any: # method call is use for create objects without name of class.(line 116)
        self.length = length 

# base, height, side1, side2
class Traingle (Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def calculate_area(self):
        self.area = (self.base * self.height) / 2

    def calculate_perimeter(self):
        self.perimeter = self.base + self.side1 + self.side2
# diameter1, diameter2, length
class Rhombus(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def calculate_area(self):
        self.area = (self.diameter1 * self.diameter2) / 2

    def calculate_perimeter(self):
        self.perimeter = self.length * 4

# length, height
class Parallelogram(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def calculate_area(self):
        self.area = self.length * self.height

    def calculate_perimeter(self):
        self.perimeter = self.length * 4

# height, base, top, side1, side2
class Trapezium(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def calculate_area(self):
        self.area = (self.top + self.base ) * self.height * 1/2

    def calculate_perimeter(self):
        self.perimeter =  self.base + self.top + self.side1 + self.side2

# radius
class Circle(Shape):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def calculate_area(self):
        self.area = self.redius **2 * 3.14
    def calculate_perimeter(self):
        self.perimeter = self.redius * 2

r = Shape()
r = Rectangle(length=2, width=4)
r.calculate_area()
r.calculate_perimeter()
r.show()
print(30 * "*")

s = Shape()
s = Square(length=3)
s.calculate_area()
s.calculate_perimeter()
s.show()# use method call
print(30 * "*" + "by method call")
s(5)
s.calculate_area()
s.calculate_perimeter()
s.show()
print(30 * "*")

t = Shape()
t = Traingle(base = 3, height =4, side1 =5, side2=6)
t.calculate_area()
t.calculate_perimeter()
t.show()
print(30 * "*")

rh = Shape()
rh = Rhombus(diameter1 =3 , diameter2=4, length=5)
rh.calculate_area()
rh.calculate_perimeter()
rh.show()
print(30 * "*")

rh = Shape()
rh = Rhombus(diameter1 =3 , diameter2=4, length=5)
rh.calculate_area()
rh.calculate_perimeter()
rh.show()
print(30 * "*")


rh = Shape()
rh = Parallelogram(length=5, height =6)
rh.calculate_area()
rh.calculate_perimeter()
rh.show()
print(30 * "*")


tr = Shape()
tr = Trapezium(height =2, base=3, top=4, side1=5, side2=6)
tr.calculate_area()
tr.calculate_perimeter()
tr.show()
print(30 * "*")

c = Shape()
c = Circle(redius = 3)
c.calculate_area()
c.calculate_perimeter()
c.show()
print(30 * "*")