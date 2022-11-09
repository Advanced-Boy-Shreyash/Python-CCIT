# No from 1 to 100 which are Divisible by 2 or 3

a = 1
while a <= 100:
    if a % 2 == 0 or a % 3 == 0:
        print(a)
    a += 1

# No from 1 to 100 which are Divisible by 5

a = 1
while a <= 100:
    if a % 5 == 0:
        print(a)
    a += 1
