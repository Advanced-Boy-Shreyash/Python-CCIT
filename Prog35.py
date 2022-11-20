# To Print Following Output
'''
        *
       * *
      * * *
     * * * *
    * * * * *
     * * * *
      * * *
       * *
        * 
'''

for j in range(1, 6):
    for k in range(9-j, 1, -1):
        print(end=" ")
    for i in range(1, j+1):
        print("*", end=" ")
    print()

for j in range(5, 1, -1):
    for k in range(10-j, 1, -1):
        print(end=" ")
    for i in range(1, j):
        print("*", end=" ")
    print()
