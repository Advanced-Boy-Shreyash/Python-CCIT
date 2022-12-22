# Methods Returning Values

# To Create 2 Rectangles and Display their Area and Perimeter

class Rectangle:
    def setDimension(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        a = self.length*self.breadth
        return a


a = Rectangle()
b = Rectangle()
a.setDimension(5, 7)
b.setDimension(10, 20)
z = a.area()+b.area()
print("Area of a is ", a.area())
print("Area of b is ", b.area())
print("Total area of Both Rectangle is", z)

print()

# To Create 2 Worker and Show Data and Payment of Both Worker


class Worker:
    def setData(self, nm, w, d):
        self.Name = nm
        self.Wages = w
        self.WDays = d

    def showData(self):
        return self.Name, self.Wages, self.WDays

    def payment(self):
        p = self.Wages*self.WDays
        return p


a = Worker()
a.setData("Raja", 500, 5)
print(a.showData(), "is Data of Raja")
print(a.payment(), "is Payment of Raja")

b = Worker()
b.setData("Gaja", 400, 8)
print(b.showData(), "is Data of Gaja")
print(b.payment(), "is Payment of Gaja")

z = a.payment()+b.payment()
print("Combine Payment of Raja and Gaja is", z)
