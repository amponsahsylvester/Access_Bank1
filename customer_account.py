class CustomerAccount:
    """"This is a blueprint for a customer"""

    def __init__(self, balance=0.0):
        self.balance = balance
        print("The account is created ")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return self.balance
