class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance =  0
    def deposit(self, amount):
        self.amount = amount
        if amount < initial_balance:
            return "invalid amount"
        else:
            return account_balance + amount
    def withdraw(self, amount):
        if amount < account_balance:
            return account_balance - amount
        else:
            return "insufficient balance"
    def display_balance(self, amount):
        print(f"Current Balance:"{account_balance})
