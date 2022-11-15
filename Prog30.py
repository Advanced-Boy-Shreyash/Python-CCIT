# Prime no.

n = int(input("Enter a no. : "))
for i in range(2, n):
    if n % i == 0:
        print("No. is Not Prime")
        break
else:
    print("No. is Prime")

# OR

flag = 0
for i in range(2, n):
    if n % i == 0:
        flag = 1
if flag == 0:
    print("No. is Prime")
else:
    print("No. is Not Prime")

# OR

count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print("No. is Prime")
else:
    print("No. is Not Prime")
