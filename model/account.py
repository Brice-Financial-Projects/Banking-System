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
        #Step 1.  Check database for the last customer ID
        max_id = 0
        for cust_id in accounts_db.keys():
            if cust_id > max_id:
                cust_id = max_id
        
        # Step 2:  Assign next customer ID to the new customer.
        new_cust_id = cust_id + 1
        accounts_db[new_cust_id] = {
            'first_name' : first_name,
            'last_name' : last_name,
        }
        return new_cust_id

    def check_for_account(self, first_name, last_name):
        """Checks database for an existing account"""
        for last_name, first_name in accounts_db.values():
            if last_name in accounts_db.values() and first_name in accounts_db.values():
                print(f'{first_name} {last_name} already exists in the database.')
                pass
            else:
                self.create_cust_id(first_name, last_name)
    
    
    def create_account(self, first_name, last_name):
        """Creates an account"""
        temp_account = []
        for acct in range(1,13):
            acct.random.randint(0,9)
            temp_account.append(acct)
        print(temp_account)
            


bank_account = BankAccount("Brice" , "Nelson")
brice = "Brice"
nelson = "Nelson"
bank_account.create_account(brice, nelson)
