# Print Salary of Person and Print Grade

s = int(input("Enter Salary : "))

if s >= 50000:
    print("Grade A")
elif 25000 <= s < 50000:
    print("Grade B")
elif 15000 <= s < 25000:
    print("Grade C")
else:
    print("Grade D")
