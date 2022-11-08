# No. is +ve or not. If +ve Check Even or Odd

num = int(input("Enter a no. : "))

if num > 0:
    print("No. is +ve")
    if num % 2 == 0:
        print(num, " is Even")
    else:
        print(num, " is Odd")
else:
    print("No. is -ve")
