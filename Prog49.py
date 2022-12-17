# Function Variable/Aliases/References

def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f


factorial = fact  # Using Function as a variable
print("Factorial is", factorial(5))
