"""banking/transactions.py"""

from db.accounts_store import transactions_db

class AccountTransactions:
    """
    Class to handle account transactions.
    Methods:
        - balance
        - deposit
        - withdraw
    """

    def __init__(self, cust_id):
        """"Initializes the AccountTransactions class"""
        self.cust_id = cust_id


    def balance(self):
        """checks balance in the db and returns the current balance"""
        if self.cust_id in transactions_db:
            balance = transactions_db[self.cust_id]['balance']
            print(f'${balance}')
            return balance
        else:
            raise ValueError(f'Customer ID {self.cust_id} not found in the database')


cust_id = '1001'
account_transactions = AccountTransactions(cust_id)

try:
    account_transactions.balance()
except ValueError as e:
    print(f'Error: {e}')