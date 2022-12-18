# Recursion Function

def message():
    print("Hello ...")
    message()


# message()

# Factorial Using Recursion Function

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


No = int(input("Enter a No. :"))
x = fact(No)
print("Factorial is", x)
