# Read a 4 digit Int and Print Sum of its Digits

# a = input("Enter a 4 digit no. : ")
# m = int(m)
# n = int(n)
# o = int(o)
# p = int(p)

#  s=m+n+o+p
#  p0rint(s)

a = input("Enter a 4 digit no. : ")
a = int(a)
x = a//1000 #taking flour division of thousand place digit
y = (a-x*1000)//100
z = (a-x*1000-y*100)//10
w = a-x*1000-y*100-z*10
print (x,y,z,w)
print("Sum of all digits of no. is ", x+y+z+w)
