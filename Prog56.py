# Conditional Case Value

# To Read Salary and Print Grade

sal = int(input("Enter Salary :"))
match sal:
    case sal if sal >= 50000:
        print("A Grade")
    case sal if sal >= 25000:
        print("B Grade")
    case sal if sal >= 15000:
        print("C Grade")
    case _:
        print("D Grade")

# To Read Percentage and Print Result

n = int(input("Enter your Percentage : "))
match n:
    case n if n >= 75:
        print("Passed with DT")
    case n if n >= 60:
        print("Passed with 1st Class")
    case n if n >= 40:
        print("Passed")
    case n if n < 40:
        print("Fail")
