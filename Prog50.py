# Nested Functions

def area(r):
    def square(n):
        s = n*n
        return s
    a = 3.14*r**2
    return a


print("Area of Circle is ", area(5))
