# Check no is 2 Digit or not. If 2 Digit check both no. are Same

a = int(input("Enter no. : "))

if a >= 10 and a <= 99:
    print("No. is 2 Digit")
    t = a//10  # Tens Place
    u = a % 10  # Unit Place
    if t == u:
        print("Both digits are Same in", a)
    else:
        print("Both digits are Different in", a)

else:
    print("No. is not a 2 Digit")
