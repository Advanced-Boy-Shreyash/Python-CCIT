a, b, c = input("Enter a b c : ").split()
a = int(a)
b = int(b)
c = int(c)

if a+b+c == 180:
    print("a b c Forms a Triangle")
    if (a == b and b == c):
        print("it is a equilateral Triangle")
    if (a == 90 or b == 90 or c == 90):
        print("it is a rt. angle Triangle")
    if (a == b or a == c or b == c):
        print("it is a isosceles Triangle")
else:
    print("It does not form a Triangle")
