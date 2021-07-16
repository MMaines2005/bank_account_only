class BankAccount:
    def __init__(self, balance=0, int_rate=0.02):
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