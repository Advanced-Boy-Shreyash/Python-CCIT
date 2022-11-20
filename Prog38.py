# Function to Calculate Simple Intrest

def si(p, n, r):
    si = (p*n*r)/100
    print("The Simple Intrest is", si)


p = int(input("Enter Principle : "))
n = float(input("Enter No of Years : "))
r = float(input("Enter Rate of Intrest : "))

si(p, n, r)


# Function to Calculate Volume of Cuboid

def vol(l, b, h):
    vol = l*b*h
    print("The Volume is", vol)


l = int(input("Enter Length : "))
b = int(input("Enter Breadth : "))
h = int(input("Enter Height : "))

vol(l, b, h)

# Function to Calculate Volume of Sphere


def vol(r):
    vol = 4/3*3.14*r**3
    print("The Volume is", vol)


r = float(input("Enter Radius of Sphere : "))
vol(r)
