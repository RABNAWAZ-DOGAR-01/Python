class Account:
    def __init__(self , Balance , Account_number):
        self.Balance = Balance
        self.Account = Account_number

    
    def debit(self , Amount):
        self.Balance -= Amount
        print(f"Rs. {Amount} has been debited from your account")
        print(f"Total Balance = {self.Balance}")




    def credit(self , Amount):
        self.Balance += Amount
        print(f"Rs. {Amount} has been credited to your account")
        print(f"Total Balance = {self.Balance}")

    def get_balance(self):
        return self.Balance
    



acc1 = Account(1000 , 123456789)
acc1.debit(100)
acc1.credit(2600)




    




    



    




    

        















    