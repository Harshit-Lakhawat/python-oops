from abc import ABC, abstractmethod

class Shapes:

    @abstractmethod
    def area(self):
        pass


class Circle(Shapes):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2

class Square(Shapes):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side*self.side

class Triangle(Shapes):
    def __init__(self, height, base):
        self.height = height
        self.base = base
    def area(self):
        return self.base*self.height*0.5

shapes = [Circle(5),Square(6),Triangle(6,10)]

for shape in shapes :
    print(shape.area())

