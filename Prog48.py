# Function Decorator

# def smart(func):
    # def advfn(a,b):
        # if a==0 or b==0:
            # return "Cannot Divide by Zero"
        # else:
            # return "func"
        # return advfn
# 
# @smart
# def div(a,b):
    # return a/b
# 
# print(div(10,3))

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
