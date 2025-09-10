a = int(input("enter number between 1 to 10:"))

match a:
    case 1:
        print("you won a charger")
    case 5:
        print("you won 100 doller")
    case 7:
        print("you won a camera")
     case _:
        print("better luck next time")