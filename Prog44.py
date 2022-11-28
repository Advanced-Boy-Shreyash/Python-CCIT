# Function with Arbitary Argumements

# Function to Display all Arguments


def disp(*args):
    print(args)


'''
def disp(*args):
    for n in args:
        print(n, end=" ")
    print()
'''

disp(12, 45, 54, 54, 456, 8, 87, 3, 45, 87, 453, 56)
disp(8, 8, 86, 897, 53, 56, 85, 564, 53, 9, 9, 96, 8, 6, 56, 8, 56)
disp(456, 89, 23, 24, 6, 63, 3, 6, 49, 45, 98)
print()

# Function Sum to Find Sum of all Arguments


def sum(*args):
    s = 0
    for i in args:
        s += i
    print("Sum is", s)


sum(12, 45, 54, 54, 456, 8, 87, 3, 45, 87, 453, 56)
sum(8, 8, 86, 897, 53, 56, 85, 564, 53, 9, 9, 96, 8, 6, 56, 8, 56)
sum(456, 89, 23, 24, 6, 63, 3, 6, 49, 45, 98)
print()

# Function Sum to Find Sum of all Even nos from Arguments


def sum(*args):
    s = 0
    for i in args:
        if i % 2 == 0:
            s += i
    print("Sum of all Even Nos :", s)


sum(12, 45, 54, 54, 456, 8, 87, 3, 45, 87, 453, 56)
sum(8, 8, 86, 897, 53, 56, 85, 564, 53, 9, 9, 96, 8, 6, 56, 8, 56)
sum(456, 89, 23, 24, 6, 63, 3, 6, 49, 45, 98)
print()

# Function Sum to Find Sum of all Even nos from Arguments


def sum(*args):
    s1 = 0
    s2 = 0
    for i in args:
        if i % 2 == 0:
            s1 += i
        else:
            s2 += i
    print("Sum of all Even Nos is", s1)
    print("Sum of all Odd Nos is", s2)


sum(12, 45, 54, 54, 456, 8, 87, 3, 45, 87, 453, 56)
sum(8, 8, 86, 897, 53, 56, 85, 564, 53, 9, 9, 96, 8, 6, 56, 8, 56)
sum(456, 89, 23, 24, 6, 63, 3, 6, 49, 45, 98)
