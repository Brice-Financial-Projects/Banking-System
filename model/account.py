"""banking/bank_account.py"""

import random
from db.accounts_store import accounts_db


class BankAccount:
    """
    This class will perform the following:

    - A constructor that takes `owner_name` and an optional `starting_balance` (default to 0).
    - A 'create_account' method that adds a new account to the database.
    - A 'close_account' method that closes the account from the database.
    - A `deposit(amount)` method that adds money to the balance.
    - A `withdraw(amount)` method that subtracts money from the balance, unless it would go negative.
    - A `get_balance()` method that returns the current balance.
    - Raise a custom `OverdraftError` if the user tries to withdraw more than the balance.
    """

    def __init__(self, first_name, last_name):
        """initialize BankAccount class"""
        self.first_name = first_name
        self.last_name = last_name
                
    def create_cust_id(self, first_name, last_name):
        """checks for the last customer ID created and creates the next ID in sequential order."""

    
    def create_account(self, first_name, last_name):
        """Checks for account in accounts, then creates an account if none exists"""
        full_name = self.first_name + self.last_name
        if full_name in self.accounts:
            raise f'{full_name} has an existing account already'
        else:
            temp_account = []
            for acct in range(1,13):
                acct.random.randint(0,9)
                temp_account.append(acct)
            print(temp_account)
            


bank_account = BankAccount()
brice = "Brice"
nelson = "Nelson"
bank_account.create_account(brice, nelson)