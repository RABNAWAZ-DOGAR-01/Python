def Calculater():
    print("Welcon to The Calcuater Program!")
    print("Please enter two numbers to perform calculations.")

    try:
        num1 = float(input("Enter the first number: "))
        Oparator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if Oparator == "+":
            result = num1 + num2
        elif Oparator == "-":
            result = num1 - num2
        elif Oparator == "*":
            result = num1 * num2
        elif Oparator == "/":
            result = num1 / num2
        else:
            print("Invalid operator!")
            return
        
        print(f"The result of {num1} {Oparator} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by Zero!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Execution completed.")

    


Calculater()

   




