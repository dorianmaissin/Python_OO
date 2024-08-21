from account import Account

class Saving_Account(Account):
    def __init__(self, owner, sold=0):
        super().__init__(owner, sold)
        