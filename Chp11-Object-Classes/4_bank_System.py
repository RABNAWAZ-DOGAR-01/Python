class Account:
    def __init__(self , account_number , balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []



    def debit(self , amount):
        try:
            if amount <= 0:
                raise ValueError("Debit amount must be positive")
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= amount
            self.transaction_history.append(f"Debited: Rs. {amount}")
            print(f"Rs. {amount} has been debited from your account")
            print(f"Total Balance = {self.balance}")
        except ValueError as e:
            print(e)


    def credit(self , amount):
        try:
            if amount <= 0:
                raise ValueError("Credit amount must be positive")
            self.balance += amount
            self.transaction_history.append(f"Credited: Rs. {amount}")
            print(f"Rs. {amount} has been credited to your account")
            print(f"Total Balance = {self.balance}")
        except ValueError as e:
            print(e)


    def get_balance(self):
        print(f"Your current balance is: Rs. {self.balance}")
        return self.balance
    

    def get_get_transaction_history(self):
        print(f"Transaction History")
        for transaction in self.transaction_history:
            print(transaction)
    



acc1 = Account(123456789, 90000)

acc1.debit(5000)
acc1.debit(4000)
acc1.credit(3070)
acc1.credit(0)
    

acc1.get_balance()
acc1.get_get_transaction_history()



            
        
        


