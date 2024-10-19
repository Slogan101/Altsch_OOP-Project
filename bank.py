

class Account():
    def __init__(self, account_number, account_type, balance, account_holder) -> None:
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            rem_balance = self.balance - amount
            self.balance = rem_balance
            return self.balance
            
        else:
            return "Insufficient Fund"

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def get_account_type(self):
        return self.account_type

    def get_account_details(self):
        return {
            "Account name": self.account_holder,
            "Account number": self.account_number,
            "Acoount type": self.account_type,
            "Account balance": self.balance,
        }


class SavingsAccount(Account):
    def get_account_details(self):
         return {
            "Account name": self.account_holder,
            "Account number": self.account_number,
            "Acoount type": self.account_type,
            "Account balance": self.balance,
            "Extra": "This is for students",
        }
    
class CurrentAccount(Account):
    def get_account_details(self):
         return {
            "Account name": self.account_holder,
            "Account number": self.account_number,
            "Acoount type": self.account_type,
            "Account balance": self.balance,
            "Extra": "This is for salary earners.",
        }