class shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"it is {self.color} ")

class circle(shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius
    def describe(self):
        #super().describe()
        print(f"it is a circle of area : {3.14*self.radius*self.radius}")
        #super().describe()
class square(shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class triangle(shape):
    def __init__(self, color, is_filled, width,height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = circle(color = 'red', is_filled = True, radius = 5)
print(circle.color)
square = square(color = "blue", width = 10, is_filled = False)
print(square.width)
print(square.is_filled)

circle.describe()
