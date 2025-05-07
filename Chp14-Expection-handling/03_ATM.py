def ATM():
    balance = 1000
    print("Welcome to the ATM!")


    try:
        amount = int(input("Enter the amount to withdraw:"))


        if amount <= 0:
            print("Insufficient balance!")
        elif amount > balance:
            print("Invalid amount!")
        else:
            balance -= amount
            print(f"Withdrawal successful! Your new balance is: {balance}")
    except ValueError:
        print("Invalid input! Please enter a number.")
    finally:
        print("Thank you for using the ATM!")


ATM()
