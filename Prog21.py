# Get Marks in 5 Sub and Check Student is Pass or Fail and Print Grade

a, b, c, d, e = input("Enter Marks in 5 Subs out of 100 : ").split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

if a >= 40 and b >= 40 and c >= 40 and d >= 40 and e >= 40:
    T = a+b+c+d+e
    P = (T/500)*100
    print("Great! You are Passed with ")
    if P > 80:
        print(f"Grade A and You have Total Marks {T} and Percent {P}.")
    elif P > 60:
        print(f"Grade B and You have Total Marks {T} and Percent {P}.")
    elif P > 50:
        print(f"Grade C and You have Total Marks {T} and Percent {P}.")
    elif P > 40:
        print(f"Grade D and You have Total Marks {T} and Percent {P}.")
else:
    print("You are Fail")
