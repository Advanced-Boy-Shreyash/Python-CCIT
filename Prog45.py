# Function to Calculate Simple Interest for n no. of Years

def interest(p, r, *years):
    for n in years:
        si = (p*r*n)/100
        print("Interest for", n, "Years is", si)


interest(5000, 10.25, 1, 3, 5, 10)
print()

# Function to Print Result of Students


def result(nm, *marks):
    t = 0
    c = 0
    for mk in marks:
        t = t+mk
        c = c+1
    print("Name is", nm)
    print("Total Marks is", t)
    print("Percentage is", t/c)


result("Amit Jain", 45, 55, 55, 50, 45)
result("Raj Joshi", 60, 45, 55, 55, 50, 45, 46)

# OR

# def results(name, branch, roll, *marks):
#     print("Marks of", name, "of Branch", branch,
#           "having Roll", roll, "is", marks)
#     s = 0
#     for m in marks:
#         s = s+m
#         p = (s/500)*100
#     if p > 35:
#         print("You are Passed with Total Marks", s, "& You have", p, "Percent")
#     else:
#         print("You are Not Passed")
#     print()


# results('Shreyash', 'AI & DS', 'AIDSU21065', 54, 68, 56, 97, 52)
# results('Shivam', 'AI & DS', 'AIDSU21063', 87, 97, 99, 52, 54)
# results('Shlok', 'AI & DS', 'AIDSU21064', 50, 85, 30, 54, 30)
# results('Samyak', 'AI & DS', 'AIDSU21061', 41, 15, 12, 54, 21)
# results('Sanchit', 'AI & DS', 'AIDSU21062', 87, 54, 21, 24, 58)
