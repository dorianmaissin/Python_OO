from account import Account

class Current_Account(Account):
    def __init__(self,name, interest, owner, balance=0):
        super().__init__(owner, balance)
        self.name = name
        self.interest_rate = interest