# Named/Keyword Arbitary Arguments

# Function to Show all Keyword & their Values that are Passed while Calling the Function

def display(**kwargs):
    print(kwargs)


display(fn='Amit', ln='Jain')
display(nm='Amit Jain', city='Amravati', contact=9876543210)

# Function to Show all Keywords & their Values are Passed while Calling the Function


def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


display(fn='Amit', ln='Jain')

# Function to Display Data of Students


def result(rn, nm, **marks):
    print("Roll no. :")
    print("Name :")
    for sub, marks in marks.items():
        print(sub, ":", marks)


result(4117, "Amit Jain", eng=67, hin=74, mar=45, math=95, sci=78)
result(3021, "Raj Joshi", M1=87, M2=73, ED=53, Py=67, Cm=95, EE=66)
