class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance =  0
    def deposit(self, amount):
        if amount < self.initial_balance:
            return "invalid amount"
        else:
            return self.account_balance + amount
    def withdraw(self, amount):
        if amount > self.account_balance:
            return "insufficient funds"
        else:
            return self.account_balance - amount
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
