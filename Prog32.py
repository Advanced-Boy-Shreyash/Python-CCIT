# Searching Element in a List

list = [2, 4, 5, 12, 13, 8]
a = int(input("Enter no. to Search : "))
for item in list:
    if a == item:
        print("Found")
        break
else:
    print("Not Found")
