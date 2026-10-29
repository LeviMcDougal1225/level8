
# This class manages the customer's bank account

class BankAccount:

    def __init__(self, name):

        self.balance = 0.0

        self.name = name 

        self.account_number = 12345

# Adds money to the account balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount

    def withdraw(self, amount):

        if 0 < amount <= self.balance:
            self.balance = self.balance - amount 

        else:
            print("Insufficient funds")

    def view_account(self):
        print("Name: ", self.name)
        print("Account Number: ", self.account_number)
        print(f"Current Balance: ${self.balance:.2f}")



    














    


    































