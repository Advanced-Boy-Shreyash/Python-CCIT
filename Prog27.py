# Print no. from 1 to 10

for i in range(1, 11):
    print(i)

# Print no from 10 to 1

for i in range(10, 0, -1):
    print(i)

# All Odd no from 1 to 100

for i in range(1, 101):
    if i % 2 != 0:
        print(i)

# All Even no from 1 to 100

for i in range(1, 100):
    if i % 2 == 0:
        print(i)

# All no from 100 to 1 which are not divisible by 5

for i in range(100,0,-1):
    if i % 5!=0:
        print (i)