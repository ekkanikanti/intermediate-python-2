class BankAccount:
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.starting_balance = starting_balance

    def deposit(self, money):
        self.starting_balance += money

    def withdraw(self, money):
        self.starting_balance -= money

    def get_balance(self):
        return f"{self.account_name} has a balance of ${self.starting_balance}"