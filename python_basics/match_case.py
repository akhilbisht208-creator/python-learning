n=int(input("Enter the value of n : "))

match n:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("saturday")
    case 7:
        print("Sunday")
    case _:
        print("Not a valid day")
