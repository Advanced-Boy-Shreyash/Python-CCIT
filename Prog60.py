# Member Access Operator (.)

# To Create 2 Rectangles and Display their Area and Perimeter

class Rectangle:
    def setDimension(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        a = self.length*self.breadth
        print("Area is ", a)

    def perimeter(self):
        p = 2*(self.length+self.breadth)
        print("Perimeter is", p)


a = Rectangle()
b = Rectangle()
a.setDimension(5, 7)
b.setDimension(10, 20)
a.area()
b.area()
a.perimeter()
b.perimeter()

# To Create 2 Box and Display Volume of Both Boxes


class Box:
    def setDimension(self, l, b, h):
        self.length = l
        self.breadth = b
        self.height = h

    def volume(self):
        v = self.length*self.breadth*self.height
        print("Volume is", v)


a = Box()
b = Box()
a.setDimension(2, 3, 4)
b.setDimension(4, 5, 3)
a.volume()
b.volume()

# To Create 2 Worker and Show Data and Payment of Both Worker


class Worker:
    def setData(self, nm, w, d):
        self.Name = nm
        self.Wages = w
        self.WDays = d

    def showData(self):
        print("Name is", self.Name)
        print("Wages is", self.Wages)
        print("Working Days are", self.WDays)

    def payment(self):
        p = self.Wages*self.WDays
        print(f"Payment of {self.Name} is", p)


a = Worker()
a.setData("Raja", 500, 5)
a.showData()
a.payment()

b = Worker()
b.setData("Gaja", 400, 8)
b.showData()
b.payment()
