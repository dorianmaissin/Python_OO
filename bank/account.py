from datetime import datetime as dt
from datetime import timedelta

class Account:
    def __init__(self,owner, balance=0, createdate=dt.now().date()):
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

    def interest(self, interest):
        one_year_before = self.createdate - timedelta(days=365)
        if (dt.now().date() - timedelta(days=365)) == one_year_before:
            interest = (self.balance / 100) * interest
            yearly_bonus = 0.50
            self.balance = self.balance + interest + yearly_bonus
            print(f"It has been a year since you opended your account with us your interest are {str(interest)} and we gave you a bonus of {str(yearly_bonus)}")
        else:
            print("You have not been with us for a year yet")
