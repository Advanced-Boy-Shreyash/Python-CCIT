# Function with Returning Values

# Function to Get Max no along 4 nos

def Max(a, b):
    if a > b:
        return a
    else:
        return b


a, b, c, d = input("Enter 4 nos : ").split(" ")
a = int(a)
b = int(b)
c = int(c)
d = int(d)

'''G1 = Max(a, b)
G2 = Max(c, d)
G = Max(G1, G2) '''

G = Max(Max(a, b), Max(c, d))
print("Greatest no is", G)

# Function to Calculate and Return Simple Interest from 3 arg


def interest(p, r, n):
    si = (p*r*n)/100
    return si


p = int(input("Enter Principle : "))
r = int(input("Enter Rate of Interest : "))
n = int(input("Enter No. of Years : "))

interest = interest(p, r, n)
print("Simple Interest is", interest)

# Function to Calculate and Return Volume of Box


def vol(l, b, h):
    v = l*b*h
    return v


l = int(input("Enter Length : "))
b = int(input("Enter Breadth : "))
h = int(input("Enter Height : "))

z = vol(l, b, h)
print("Volume is", z)

# Function to Calculate and Return Volume of Box


def vol(r):
    v = (4/3)*3.14*r**3
    return v


n = int(input("Enter Radius : "))

z = vol(n)
print("The Volume of Sphere is", z)
