# Import necessary classes from other modules
from bank import Bank
from account import Account
from current_account import Current_Account
from saving_account import Saving_Account

# Define a class User
class User():
    # Constructor method to initialize a User object
    def __init__(self, first_name, last_name, age, bank):
        # Initialize attributes of the User object
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.bank = bank
        # Initialize an empty list to store accounts
        self.accounts = []
    
    # Method to create a new account for the user
    def create_account(self, account_type, deposite = 0):
        # Check the type of account to create
        if account_type == "current":
            # Create a Current_Account object
            account = Current_Account("current",0.5, self, deposite)
        elif account_type == "saving":
            # Create a Saving_Account object
            account = Saving_Account("saving",2 , self, deposite)
        # Add the new account to the user's list of accounts
        self.accounts.append(account)
        # Add the new account to the bank's list of accounts
        self.bank.add_account(account)
    
    # Method to display the balance of a specific account
    def display_account(self, index):
        # Get the account at the specified index
        account = self.accounts[index]
        # Print the account name and balance
        print(f"{self.first_name} Your {account.name} account balance is: {account.display_balance()}")
    
    # Method to deposit money into a specific account
    def depostit(self, amount, account_index):
        # Get the account at the specified index
        account = self.accounts[account_index]
        # Deposit the money into the account
        account.depostit_money(amount)
        print(f"{self.first_name} You just deposit {amount} to your {account.name} account")
        
    # Method to withdraw money from a specific account
    def withdrawal(self, amount, account_index):
        # Get the account at the specified index
        account = self.accounts[account_index]
        # Withdraw the money from the account
        account.withdrawal_money(amount)
        print(f"{self.first_name} You just withdrawal {amount} from your {account.name} account")

    # Method to transfer money between two of the user's own accounts
    def send_money_own_accounts(self, amount, sending_account_name, receive_account_name):
        # Loop through the user's accounts
        for account in self.accounts:
            # Check if the account is the receiving account
            if account.name == receive_account_name:
                # Deposit the money into the receiving account
                account.depostit_money(amount)
                print(f"{self.first_name} You received {amount} from your {sending_account_name} account")
            # Check if the account is the sending account
            if account.name == sending_account_name:
                # Withdraw the money from the sending account
                account.withdrawal_money(amount)

    # Method to make a payment to another user's account
    def payment(self, sending_account_name, amount, receiver, receiver_account):
        # Loop through the user's accounts
        for account in self.accounts:
            # Check if the account is the sending account
            if account.name == sending_account_name:
                # Loop through the receiver's accounts
                for foreign_account in receiver.accounts:
                    # Check if the account is the receiving account
                    if foreign_account.name == receiver_account:
                        # Deposit the money into the receiving account
                        foreign_account.depostit_money(amount)
                        account.withdrawal_money(amount)
                        print(f"{self.first_name} You just send {amount} to {receiver.first_name} account")

    def get_interest(self, account_index):
        account = self.accounts[account_index]
        account.interest(account.interest_rate)
        





