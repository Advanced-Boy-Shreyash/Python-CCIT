# Objects

# To Create 2 Rectangles and Display their ID & Type

class Rectangle:
    def setDimension(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        a = self.length*self.breadth
        print("Area is", a)

    def perimeter(self):
        p = 2*(self.length+self.breadth)
        print("Perimeter is", p)


a = Rectangle()
b = Rectangle()
print("Print a:", a)
print("Print ID of a:", id(a))
print("Print Type of a:", type(a))
print("Print b:", b)
print("Print ID of b:", id(b))
print("Print Type of b:", type(b))

a.setDimension(5, 6)
b.setDimension(3, 7)
a.area()
a.perimeter()
b.area()
b.perimeter()
