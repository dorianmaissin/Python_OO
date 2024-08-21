from datetime import datetime as dt

class Account:
    def __intit__(self,owner, balance=0, createdate=dt.now()):
        self.balance = balance
        self.owner = owner
        self.createdate = createdate
