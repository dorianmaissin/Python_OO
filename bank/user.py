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
            account = Current_Account("current",self,deposite)
        elif account_type == "saving":
            account = Saving_Account("saving",self, deposite)
        self.accounts.append(account)
        self.bank.add_account(account)
    
    def display_account(self,index):
        print(f"{self.accounts[index].name} : {self.accounts[index].display_balance()}")
    
    def depostit(self,amount,account_index):
        self.accounts[account_index].depostit_money(amount)
        
    def withdrawal(self,amount,account_index):
        self.accounts[account_index].withdrawal_money(amount)

    def send_money_own_accounts(self,amont, sending_account_name, receive_account_name):
        for account in self.accounts:
            if account.name == receive_account_name:
                account.depostit_money(amont)

            if account.name == sending_account_name:
                account.withdrawal_money(amont)

    def payment(self,sending_account_name,amount,receiver,receiver_account):
        for account in self.accounts:
            print(account)
            print(receiver.accounts)
            if account.name == sending_account_name:
                for foreign_account in receiver.accounts:
                    if foreign_account.name == receiver_account:
                        foreign_account.depostit_money(amount)




