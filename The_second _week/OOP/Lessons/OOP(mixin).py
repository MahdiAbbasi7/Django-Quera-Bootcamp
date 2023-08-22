import logging

class PrintInfoMixin ():
    def PrintInfoMixin(self):
        print(__name__,__doc__)

class Test(PrintInfoMixin):
    pass
car = Test()
# car.PrintInfoMixin()
#----------------------------------------------------------------
class MathOperationsMixin():
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y

    def Plus(self):
        result = self.X + self.Y
        print(result)
    
    def Mines(self):
        result = self.X - self.Y
        print(result)

    def Divide(self):
        result = self.X / self.Y
        print(result)

    def Multi(self):
        result = self.X * self.Y
        print(result)

class Number(MathOperationsMixin):
    pass
        

number = Number(3,5)
# number.Plus()
# number.Mines()
# number.Divide()
# number.Multi()
#----------------------------------------------------------------

class LoggerMixin():
    def name(self):
        print(self.__class__.__name__)
    def args(self):
        all_args = locals()
        print(all_args)
    
class Example(LoggerMixin):
    def introduction(self):
        print("Name and args for class : \t")

test = Example()
test.introduction()
test.name()
test.args()

