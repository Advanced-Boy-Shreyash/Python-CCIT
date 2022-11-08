# Get Age and Gender and Check He or She is Eligible for Marriage

g = input("Enter Your Gender Code : ")
a = int(input("Enter Your Age : "))

if (g == "M" or g == "m"):
    print("Male")
    if a >= 21:
        print("You are Eligible for Marriage")
    else:
        print("You are not Eligible for Marriage")
elif (g == "F" or g == "f"):
    print("Female")
    if a >= 18:
        print("You are Eligible for Marriage")
    else:
        print("You are not Eligible for Marriage")
else:
    print("Enter Valid Input")
