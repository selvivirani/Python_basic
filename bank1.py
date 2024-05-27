import random

account = {}

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.ac_number = self.account_number()
        self.balance = balance
        account[name] = self
        print(f"Account created for {name} with account number {self.ac_number}.")

    def account_number(self):
       
        return ''.join(str(random.randint(0, 9)) for _ in range(11))

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid input for deposit amount.")
            return
        self.balance += amount
        print(f"{self.name} deposited ${amount}. Current balance: ${self.balance}")

    
    def withdraw(self, amount):
       while True:
        try:
            amount = float(amount)
        except ValueError:
            print("Invalid input for withdrawal amount.")
            return
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name} withdrew ${amount}. Current balance: ${self.balance}")
            break  
        else:
            print("You don't have enough funds to withdraw.")
            try:
                amount = float(input("Enter a new withdrawal amount: "))
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

name = input("Enter your name: ")
balance = float(input("Enter your initial balance: "))

user_account = Account(name, balance)

amount = input("Enter deposit amount: ")
user_account.deposit(amount)

withdrawal_amount = input("Enter withdrawal amount: ")
user_account.withdraw(withdrawal_amount)