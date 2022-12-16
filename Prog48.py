# Function Decorator

def decorator(fn):
    def advfn():
        print("--------------------")
        fn()
        print("--------------------")
    return advfn()


@decorator
def ccit():
    print("CCIT")
    print("Rajapeth")
    print("Amravati")


@decorator
def welcome():
    print("Good Morning")


welcome()
print()
ccit()
