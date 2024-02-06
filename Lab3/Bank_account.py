class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")


owner = input("Enter the account owner's name: ")
initial_balance = float(input("Enter the initial balance: "))
account = BankAccount(owner, initial_balance)

deposit_amount = float(input("Enter the deposit amount: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter the withdrawal amount: "))
account.withdraw(withdraw_amount)


invalid_withdrawal_amount = float(input("Enter an invalid withdrawal amount: "))
account.withdraw(invalid_withdrawal_amount)