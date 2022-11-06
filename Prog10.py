# To check if the no. is 2 Digit and make sum of its 2 digits

a = int(input("Enter a no. : "))
if a >= 10 and a < 100:
    print("No. is a 2 Digit no.")
    x = a % 10 #Unit Place
    y = a//10 #Tens Place

    s = x+y
    print(x, y)
    print(s)

else:
    print("No. is not a 2 Digit no.")
