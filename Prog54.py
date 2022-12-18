# Structural Pattern Matching/Matching Case Statement

# WAP to Read a Single Digit No. and Print it in Words

n = int(input("Enter a Single Digit No. : "))
match n:
    case 0: print("The No. is Zero")
    case 1: print("The No. is One")
    case 2: print("The No. is Two")
    case 3: print("The No. is Three")
    case 4: print("The No. is Four")
    case 5: print("The No. is Five")
    case 6: print("The No. is Six")
    case 7: print("The No. is Seven")
    case 8: print("The No. is Eight")
    case 9: print("The No. is Nine")
    case _: print("Invalid Input")

# WAP to Read No. of Month and Print it in Words

n = int(input("Enter No. of Month : "))
match (n):
    case 1: print("Jan")
    case 2: print("Feb")
    case 3: print("Mar")
    case 4: print("Apr")
    case 5: print("May")
    case 6: print("Jun")
    case 7: print("Jul")
    case 8: print("Aug")
    case 9: print("Sep")
    case 10: print("Oct")
    case 11: print("Nov")
    case 12: print("Dec")
    case _: print("Enter Valid Input")
