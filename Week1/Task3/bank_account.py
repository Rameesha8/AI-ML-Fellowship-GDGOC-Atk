# bank_account.py

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder      # Encapsulation
        self._balance = balance                   # Protected variable

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self._balance}")
        else:
            print("Insufficient balance.")

    def __str__(self):  # Magic method
        return f"Account Holder: {self.account_holder}, Balance: {self._balance}"


# Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    # Polymorphism (method override)
    def deposit(self, amount):
        interest = amount * self.interest_rate
        total = amount + interest
        self._balance += total
        print(f"Deposited with interest: {total}. Balance: {self._balance}")


# Testing
if __name__ == "__main__":
    acc1 = BankAccount("Rameesha", 1000)
    acc1.deposit(500)
    acc1.withdraw(300)
    print(acc1)

    acc2 = SavingsAccount("Rameesha Savings", 2000)
    acc2.deposit(500)
    print(acc2)
