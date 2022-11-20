# Logic Building Programme of * in for Loop

# To Print ' * * * * * ' in 5 Lines

for j in range(1, 6):
    for i in range(1, 6):
        print("*", end=" ")
    print()
print()

# To Print ' * ' ... ' * * * * * '

for j in range(1, 6):
    for i in range(1, j+1):
        print("*", end=" ")
    print()
print()

# To Print ' * * * * * ' ... ' * '

for j in range(5, 0, -1):
    for i in range(1, j+1):
        print("*", end=" ")
    print()
print()

# To Print ' 5 * * * * * ' ; ' 4 * * * * ' ... ' 1 * '

for j in range(5, 0, -1):
    print(j, end=" ")
    for i in range(1, j+1):
        print("*", end=" ")
    print()
print()
