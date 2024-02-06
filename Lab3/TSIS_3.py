class String:

    def getstring(self):
        self.s = input()
    
    def printstring(self):
        print(self.s.upper())
    
p = String()

p.getstring()
p.printstring()

class Shape:
    def __init__(self):
        pass 
    def area(self):
        return 0  
    
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length ** 2 

user_length = float(input("Enter the length of the square: "))
square_instance = Square(user_length)

print("Area of the square:", square_instance.area())

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

user_length = float(input("Enter the length of the rectangle: "))
user_width = float(input("Enter the width of the rectangle: "))
rectangle_instance = Rectangle(user_length, user_width)

print("Area of the rectangle:", rectangle_instance.area())