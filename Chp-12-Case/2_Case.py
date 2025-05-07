day = int(input("Select your day 1 - 7  " ))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Sturday")
    case 7:
        print("Sunday")
        




num1 = input("Enter your First number")
num2 = input("Enter your Second number")
op = input("Enter operator (+, -, *, /): ")


match op:
    case "+":
        print(f"Result {num1 + num2}")
    case "-":
        print(f"Result {num1 - num2}")
    case "*":
        print(f"Result {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"Result {num1 / num2}")
        else:
            print("Cannot divide by zero!")
    case _:
        print("Invalid operator")
       
