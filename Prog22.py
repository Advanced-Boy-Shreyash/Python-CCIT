# Check Greatest among 4 no. Using Ternary Operator

a, b, c, d = input("Enter 4 no. : ").split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)

x = a if a > b else b
y = c if c > d else d
z = print(x, "is Greatest")if x > y else print(y, "is Greatest")
