# Keyword Arguments

# Function to Calculate Simple Interest and Print it According to Argument Values

def interest(p, r, n):
    si = (p*r*n)/100
    print("Simple Interest is", si)


interest(5000, 10.25, 3)
interest(p=5000, r=10.25, n=3)
interest(r=10.25, p=5000, n=3)
interest(n=3, p=5000, r=10.25)

# Function to Print Roll no. and name which is Passed as Argument


def display(rn, nm):
    print("Roll no: ", rn)
    print("Name :", nm)


display(4118, 'Amit Jain')
display(rn=4118, nm='Amit Jain')
display(nm='Amit Jain', rn=4118)
