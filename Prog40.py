# Function to Check no is Prime

def prime(a):
    for i in range(2, a):
        if a % i == 0:
            print("No is Not Prime")
            break
    else:
        print("No is Prime")


a = int(input("Enter no. : "))
prime(a)

# Function to Print Max and Min in 2 nos


def max(a, b):
    if a > b:
        print(a, "is Greatest")
    else:
        print(b, "is Greatest")


a = int(input("Enter a : "))
b = int(input("Enter b : "))
max(a, b)
