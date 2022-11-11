# Read a no. and Print all no from 1 to that no.

a = int(input("Enter a End Point : "))
for i in range(1, a+1):
    print(i)

# Read a no. and Print all no from that no. to 1

a = int(input("Enter a Start Point : "))
for i in range(a, 0, -1):
    print(i)

# Read a and b and Print all no. from a to b

a = int(input("Enter a Start Point : "))
b = int(input("Enter a End Point : "))
for i in range(a,b+1):
    print(i)