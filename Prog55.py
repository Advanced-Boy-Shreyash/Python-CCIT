# WAP to Read Shirts Size Code and Print Output According to Given Criteria [s-small,m-medium,l-large]

size = input("Enter Shirt Size Code : ")
match size:
    case 's' | 'S': print("Size is Small")
    case 'm' | 'M': print("Size is Medium")
    case 'l' | 'L': print("Size is Large")
    case _: print(f"Cannot Find {size} Shirt")

# WAP to Read Colour Code and Print Output According to Given Criteria [r-red,b-blue,g-green]

n = input("Enter Colour Code : ")
match(n):
    case 'r' | 'R': print("Colour is Red")
    case 'b' | 'B': print("Colour is Blue")
    case 'g' | 'G': print("Colour is Green")
    case _: print("White")
