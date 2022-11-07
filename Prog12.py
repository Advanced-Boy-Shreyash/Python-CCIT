# Find Greatest among 3 no.

a, b, c = input("Enter 3 no. : ").split()
a=int(a)
b=int(b)
c=int(c)

if a > b and a > c:
    print(a, " is greatest")
elif b > a and b > c:
    print(b, " is greatest")
else:
    print(c, " is greatest")
