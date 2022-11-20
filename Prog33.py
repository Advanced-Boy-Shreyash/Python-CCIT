# Logic Building Programme in for Loop

# To Print all no from 1 to 10 upto 5 Times

for j in range(1, 6):
    for i in range(1, 11):
        print(i, end=" ")
    print()
print()

#  To Print ' 5 4 3 2 1 ' Four Times

for j in range(1, 5):
    for i in range(5, 0, -1):
        print(i, end=" ")
    print()
print()

# To Print ' 1 1 1 1 1 ' ... ' 5 5 5 5 '

for j in range(1, 6):
    for i in range(1, 6):
        print(j, end=" ")
    print()
print()

# To Print ' 1 ' ; ' 1 2 ' ... ' 1 2 3 4 5 '

for j in range(1, 6):
    for i in range(1, j+1):
        print(i, end=" ")
    print()
print()

# To Print ' 1 2 3 4 5 ' ; ' 1 2 3 4' ... ' 1 '

for j in range(5, 0, -1):
    for i in range(1, j+1):
        print(i, end=" ")
    print()
print()

# To Print ' 5 ' ; ' 5 4 ' ... ' 5 4 3 2 1 '

for j in range(5, 0, -1):
    for i in range(5, j-1, -1):
        print(i, end=" ")
    print()
print()

# To Print ' 5 4 3 2 1 ' ; ' 4 3 2 1 ' ; ' 1 '

for j in range(5, 0, -1):
    for i in range(j, 0, -1):
        print(i, end=" ")
    print()
print()

# To Print ' 5 4 3 2 1 ' ; ' 5 4 3 2 ' ; ' 5 '

for j in range(1, 6):
    for i in range(5, j-1, -1):
        print(i, end=" ")
    print()
print()
# To Print ' 1 2 3 4 5 ' ; ' 2 3 4 5 ' ... ' 5 '

for j in range(5, 0, -1):
    for i in range(j, 6):
        print(i, end=" ")
    print()
print()

# Table Building from 1 to 10

for j in range(1, 11):
    for i in range(1, 11):
        print(i*j, end=" ")
    print()
print()
