# Find Sum of all no. from 1 to Given no.

a = int(input("Enter End Point : "))
s = 0
for i in range(1, a+1):
    s = s+i
print(s)

# Sum of Even no in a List Collection

arr = [10, 15, 16, 22, 32, 11, 4, 1]
s = 0
for i in arr:
    if i % 2 == 0:
        s = s+i
print(s)

# Sum of Even no in a List Collection

arr = [10, 15, 16, 22, 32, 11, 4, 1]
s = 0
for i in arr:
    if i % 2 != 0:
        s = s+i
print(s)

# Count all Even nos in a List Collection

arr = [10, 15, 16, 22, 32, 11, 4, 1]
c = 0
for i in arr:
    if i % 2 == 0:
        c += 1
print(c)

# Count all Persons who are Eligible for Voting

age = [45, 54, 8, 8, 7, 65, 45, 21, 5, 4, 74]
c = 0
for v in age:
    if v > 18:
        c += 1
print(c)
