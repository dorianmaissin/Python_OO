from bank import Bank
# from account import Account
from user import User
# from saving_account import Saving_account
# from current_account import Current_account

bank = Bank("Belfius")
bank2 = Bank("CBC")
user1 = User("Dorian", "Maissin", 31, bank)
user2 = User("Flo", "Rigau", 33, bank2)
user3 = User("Alice", "Choco", 28, bank)

user1.create_account("current")
print(user1.accounts,user1.bank,user1.accounts)