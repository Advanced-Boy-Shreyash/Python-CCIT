# Check Triangle Form or not. If form Check if it is Equilateral, Right angle, or Isosceles

a, b, c = input("Enter 3 Angles : ").split(' ')
a = int(a)
b = int(b)
c = int(c)

if a+b+c == 180:
    print(a, b, c, "Forms a Triangle")
    if a == b and b == c:
        print("Triangle is Eqilateral")
    elif (a == b or b == c or a == c):
        print("Triangle is Isosceles")
    elif (a == 90 or b == 90 or a == 90):
        print("Triangle is Right Angle")
    else:
        print("Triangle is Any Triangle")
else:
    print(a, b, c, "Not forms a Triangle")
