# Functions with Default Argument

# Function to Calculate Simple Interest from 3 arg having Default Value n=1

def interest(p, r, n=1):
    si = (p*r*n)/100
    print("Simple Interest is", si)


interest(45000, 5, 3)
interest(50000, 5)

# Function to Print Even nos From 1 to specified no. (default value of n is 100)


def even(n=100):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)


even(50)
even()

# Function sum which can be call by Passing 4,3 or 2 Arg


def sum(a, b, c=0, d=0):
    s = a+b+c+d
    print("Sum is", s)


sum(100, 200)
sum(100, 200, 300)
sum(100, 200, 300, 400)
