"""banking/transactions.py"""

from db.accounts_store import accounts_db

class AccountTransactions:
    """
    Class to handle account transactions.
    Methods:
        - balance
        - deposit
        - withdraw
    """

    def __init__(self, cust_id, balance):
        """"Initializes the AccountTransactions class"""
        self.cust_id = cust_id
        self.balance = balance

    def balance(self, cust_id):
        pass
