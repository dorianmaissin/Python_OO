from bank import Bank
from account import Account
from current_account import Current_Account
from saving_account import Saving_Account

class User():
    def __init__(self, first_name, last_name, age, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.bank = bank
        self.accounts = []
    
    def create_account(self, account_type, deposite = 0):
        if account_type == "current":
            account = Current_Account(self, deposite)
        elif account_type == "saving":
            account = Saving_Account(self, deposite)
        self.accounts.append(account)
        self.bank.add_account(account)