from bank import Bank
from account import Account

class User():
    def __init__(self, first_name, last_name, age, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.bank =bank
        self.account = []