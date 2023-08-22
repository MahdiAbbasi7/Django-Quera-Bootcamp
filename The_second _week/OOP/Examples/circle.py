# Calculate premeters for cirecles
class Circle():
    def __init__(self, radius):
        self._radius = radius
    @property
    def premeter(self):
        return f"{3.14 *self._radius * self._radius }"

    @premeter.setter
    def premeter(self, premeter):
        if premeter > 0.0:
            self._radius = premeter
        else:
            raise ValueError("Invalid redius")

test = Circle(5)
test.premeter = 1
# print(test.premeter)
# -----------------------------------------------
# Converting Celsius To Fahrenheit
class Temperature():
    def __init__(self, temperature):
        self._temperature = temperature
    def show(self):
        return f"Temperature is: {self._temperature}'C"
    @property
    def tofahrenheit(self):
        return  (self._temperature*9/5)+32
    
test1 = Temperature(5)
print(test1.show())
print(test1.tofahrenheit)

