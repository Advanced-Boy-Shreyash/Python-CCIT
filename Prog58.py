# OOPS

# Class to Print Area and Circumference of Circle

class Circle:
    def setRadius(self, r):
        self.Radius = r

    def area(self):
        a = 3.14*self.Radius**2
        print("Area is", a)

    def circumference(self):
        c = 2*3.14*self.Radius
        print("Circumference is", c)


a = Circle()
a.setRadius(5)
a.area()
a.circumference()

# Class to Print Volume of Sphere


class Sphere:
    def setRadius(self, r):
        self.Radius = r

    def volume(self):
        v = (4/3)*3.14*(self.Radius**3)
        print("Volume is", v)


a = Sphere()
a.setRadius(3)
a.volume()
