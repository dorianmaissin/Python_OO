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
user1.create_account("saving")
user2.create_account("current")
user2.create_account("saving")
user1.display_account(0)
user1.display_account(1)
user1.depostit(100,0)
user1.depostit(100,1)
user1.display_account(0)
user1.display_account(1)
user1.withdrawal(20,0)
user1.display_account(0)
user1.send_money_own_accounts(10, 'saving', 'current')
user1.display_account(0)
user1.display_account(1)
user1.payment('current', 20, user2, 'current')
user1.display_account(0)
user2.display_account(0)
user1.get_interest(1)
user1.display_account(1)