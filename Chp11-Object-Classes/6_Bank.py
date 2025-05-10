class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def debit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("❌ Debit amount must be positive.")
            if amount > self.balance:
                raise ValueError("❌ Insufficient funds.")
            self.balance -= amount
        except ValueError as e:
            print(e)
        else:
            print(f"✅ Rs. {amount} has been debited from your account.")
        print(f"💰 Total Balance = Rs. {self.Total_balance()}")

    def credit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("❌ Credit amount must be positive.")
            self.balance += amount
        except ValueError as e:
            print(e)
        else:
            print(f"✅ Rs. {amount} has been credited to your account.")
            print(f"💰 Total Balance = Rs. {self.Total_balance()}")

    def Total_balance(self):
        return self.balance


# Input Account Details
while True:
    try:
        acc_num = int(input(" Enter your Account Number: "))
        init_balance = float(input(" Enter Initial Balance: "))
        break
    except ValueError:
        print("❌ Invalid input! Please enter numeric values only.")

user_account = Account(acc_num, init_balance)

# Main Menu
while True:
    print("\n🔸 Choose an option:")
    print("1. Credit")
    print("2. Debit")
    print("3. Check Balance")
    print("4. Exit")

    choice = input(" Enter choice (1-4): ")

    if choice == "1":
        try:
            amount = float(input("💸 Enter amount to Credit: "))
            user_account.credit(amount)
        except ValueError:
            print("❌ Invalid input! Please enter numeric values only.")

    elif choice == "2":
        try:
            amount = float(input("💸 Enter amount to Debit: "))
            user_account.debit(amount)
        except ValueError:
            print("❌ Invalid input! Please enter numeric values only.")

    elif choice == "3":
        print(f"📊 Current Balance = Rs. {user_account.Total_balance()}")

    elif choice == "4":
        print(" Thank you for banking with us. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
