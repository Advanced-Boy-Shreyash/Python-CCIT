#Functions with Default Argument

# Functions to Print Area & Circumference of a Circle

def area(r):
    a = 3.14*r*r
    print("Area is", a)


def circumference(r):
    c = 2*3.14*r
    print("Circumference is", c)


r = int(input("Enter Radius : "))
area(r)
circumference(r)

# Function to Print Sum of no. upto Specified no


def sum(a):
    s = 0
    for i in range(1, a+1):
        s = s+i
    print("Sum is", s)


a = int(input("Enter No. : "))
sum(a)

# Function to Print a Factorial


def fact(a):
    f = 1
    for i in range(1, a+1):
        f = f*i
    print("Factorial is : ", f)


a = int(input("Enter No. : "))
fact(a)
