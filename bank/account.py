from datetime import datetime as dt

class Account:
    def __init__(self,owner, balance=0, createdate=dt.now()):
        self.balance = balance
        self.owner = owner
        self.createdate = createdate

    def display_balance(self):
        return self.balance
    
    def depostit_money(self,amount):
        new_balance = self.balance + amount
        self.balance = new_balance
    
    def withdrawal_money(self,amount):
        new_balance = self.balance - amount
        if new_balance < 0:
            print("Insufficient balance")
        else:
            self.balance = new_balance

    # def send_money_own_accounts(self,amont, sending_account_name, receive_account_name):
    #     for account in self.accounts:
    #         if account.name == receive_account_name:
    #             new_balance = account.balance + amont
    #             account.balance = new_balance

    #         if account.name == sending_account_name:
    #             new_balance = account.balance - amont
    #             account.balance = new_balance