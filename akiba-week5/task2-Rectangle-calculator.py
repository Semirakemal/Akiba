class Rectangle:

    def __init__(self,width,length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.length +  self.width)

rectangle1 = Rectangle(7,8)
rectangle2 = Rectangle(34,23)

print(f"Area of rectangle1: {rectangle1.area()}")
print(f"perimeter of rectangle1: {rectangle1.perimeter()}")

print()

print(f"area of rectangle2: {rectangle2.area()}")
print(f"perimeter of rectangle2: {rectangle2.perimeter()}")
