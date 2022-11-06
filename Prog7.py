# Marks of 5 Sub and Print Total Marks and Percentage

a = int(input("Enter Marks in sub a out of 100: "))
b = int(input("Enter Marks in sub b out of 100: "))
c = int(input("Enter Marks in sub c out of 100: "))
d = int(input("Enter Marks in sub d out of 100: "))
e = int(input("Enter Marks in sub e out of 100: "))

T = a+b+c+d+e
P = (T/500)*100
print("Total Marks are ", T)
print("Percentage are ", P)
