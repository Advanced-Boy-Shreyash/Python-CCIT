# No. is +ve or not. If +ve Check 2 Digit or not

a = int(input("Enter a no. : "))

if a > 0:
    print(a, " is +ve")
    if a >= 10 and a <= 99:
        print("No. is 2 Digit")
    else:
        print("No. is not a 2 Digit")
else:
    print(a, " is -ve")
