# Function as Argument

def sqr(n):
    return n*n


def cube(n):
    return n**3


def display(fn):
    for i in range(1, 11):
        print(fn(i))


print("Squares are :",end=" ")
display(sqr)
print("Cubes are :")
display(cube)
