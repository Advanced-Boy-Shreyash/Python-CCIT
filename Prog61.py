# To Create 2 Employee and Show Data and Payment of Both Employee

class Employee:
    def setData(self, n, s, a):
        self.name = n
        self.salary = s
        self.advance = a

    def showData(self):
        print("Name of Employee is", self.name)
        print("Salary of Employee is", self.salary)
        print("Advance Paid to Employee is", self.advance)

    def payment(self):
        p = self.salary-self.advance
        print(f"Payment to {self.name} is", p)


a = Employee()
a.setData("Amit", 25000, 5000)
a.showData()
a.payment()

print()

b = Employee()
b.setData("Gopal", 40000, 0)
b.showData()
b.payment()

print()

# To Create 2 Sets and Display sum, Both Sets and Mean


class Set:
    def setElement(self, x, y, z):
        self.n1 = x
        self.n2 = y
        self.n3 = z

    def mean(self):
        mean = (self.n1+self.n2+self.n3)/3
        print("Mean is", mean)

    def sum(self):
        sum = self.n1+self.n2+self.n3
        print("Sum is", sum)


a = Set()
a.setElement(2, 5, 3)
a.mean()
a.sum()

b = Set()
b.setElement(6, 10, 4)
b.mean()
b.sum()

print()

# Class Student to Display Roll no. , Name, Marks, Percentage, Result


class Student:
    def setData(self, rn, nm, m1, m2, m3, m4, m5):
        self.rollno = rn
        self.name = nm
        self.Eng = m1
        self.Hin = m2
        self.Mar = m3
        self.Mat = m4
        self.Sci = m5

    def total(self):
        t = self.Eng+self.Hin+self.Mar+self.Mat+self.Sci
        print(f"{self.name} has Total Marks : {t}")

    def percentage(self):
        p = (self.Eng+self.Hin+self.Mar+self.Mat+self.Sci)/5
        print(f"{self.name} has Percentage : {p}")

    def result(self):
        if (self.Eng > 35 and self.Hin > 35 and self.Mar > 35 and self.Mat > 35 and self.Sci > 35):
            print("You are Passed")
        else:
            print("You are Fail")


a = Student()
a.setData(4117, 'Amit Jain', 36, 54, 85, 37, 37)
a.total()
a.percentage()
a.result()

b = Student()
b.setData(4118, 'Sumit Mishra', 87, 95, 92, 86, 82)
b.total()
b.percentage()
b.result()
