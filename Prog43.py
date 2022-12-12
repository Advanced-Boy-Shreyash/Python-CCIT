# Functions to Print Area & Circumference of a Circle

def area(r):
    a = 3.14*r*r
    return a


def circumference(r):
    c = 2*3.14*r
    return c


r = int(input("Enter Radius : "))

a = area(r)
c = circumference(r)

print("Area is", a)
print("Circumference is", c)

# Function to Print Sum of no. upto Specified no


def sum(a):
    s = 0
    for i in range(1, a+1):
        s = s+i
    return s


a = int(input("Enter No. : "))
s = sum(a)
print("Sum is", s)

# Function to Print a Factorial


def fact(a):
    f = 1
    for i in range(1, a+1):
        f = f*i
    return f


a = int(input("Enter No. : "))
f = fact(a)
print("Factorial is : ", f)
