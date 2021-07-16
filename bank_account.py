class BankAccount:
    def __init__(self,int_rate,balance=0):
        self.balance = balance
        self.int_rate = int_rate
        

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <= amount:
            print("Insufficient Funds")
        return self
    def display_account_info(self):
        print(f"Your balance is: ", self.balance)
        return self

    def yield_interest(self):
        self.balance = self.balance*self.int_rate
        return self

s = BankAccount(0.02,0)
m = BankAccount(0.01, 500)

m.deposit(200).deposit(200).withdraw(100).display_account_info()
s.deposit(400).deposit(300).withdraw(800).display_account_info()