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


    def create_cust_id(self, first_name, last_name, address, city, state, zip):
        """checks for the last customer ID created and creates the next ID in sequential order."""
        # Step 0:  Check datebase for existing account
        if self.check_for_account(first_name, last_name):
            print(f"Customer {first_name} {last_name} already exists. Skipping account creation.")
            return None

        #Step 1.  Check database for the last customer ID
        max_id = 1000
        for cust_id in accounts_db.keys():
            if cust_id > max_id:
                max_id = cust_id
        
        # Step 2:  Assign next customer ID to the new customer and store customer info into a dict.
        new_cust_id_info = max_id + 1
        acct_num = self.create_account(first_name,last_name)
        accounts_db[new_cust_id_info] = {
            'first_name' : first_name,
            'last_name' : last_name,
            'acct_num': acct_num,
            'address': address,
            'city': city,
            'state': state,
            'zip': zip
        }
        return new_cust_id_info


    def check_for_account(self, first_name, last_name):
        """Checks database for an existing account"""
        for data in accounts_db.values():
            if data['first_name'] == first_name and data['last_name'] == last_name:
                print(f'{first_name} {last_name} already exists in the database.')
                return True

        print(f'{first_name} {last_name} does not exist in the database, needs a new account setup.\nRun create_cust_id')
        return False


    def create_account(self, first_name, last_name):
        """Creates an account"""

        acct = [random.randint(0,9) for x in range(12)]
        acct_num = ''.join(str(x) for x in acct)
        if acct_num in (data['acct_num'] for data in accounts_db.values()):
            return self.create_account(first_name, last_name)
        else:
            return acct_num

            


bank_account = BankAccount("Brice" , "Nelson")
brice = "Brice"
nelson = "Nelson"
address = '3650 Hampton Glen Place'
city = 'Jacksonville'
state = 'FL'
zip = '32257'

bank_account.create_cust_id(brice, nelson, address, city, state, zip)
bank_account.check_for_account(brice, nelson)
from pprint import pprint

cust_id = bank_account.create_cust_id(brice, nelson, address, city, state, zip)
pprint(accounts_db)

# print(accounts_db)
