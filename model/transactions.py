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
        """Retrieves and returns the current account balance from the database.

        This method checks if the customer ID exists in the transaction database
        and returns the current balance if found. The balance is both printed to
        the console and returned as a value.

        Returns:
            float: The current account balance.

        Raises:
            ValueError: If the customer ID is not found in the database.

        Examples:
            >>> account = AccountTransactions('1001')
            >>> account.balance()
            $71.72
            71.72
        """
        if self.cust_id in transactions_db:
            balance = transactions_db[self.cust_id]['balance']
            print(f'${balance}')
            return balance
        else:
            raise ValueError(f'Customer ID {self.cust_id} not found in the database')


    def deposit(self, deposit):
        """
        Deposits funds into the customer's account.
        
        This method adds the specified amount to the customer's current balance
        in the transaction database. If the customer ID does not exist in the 
        database, a ValueError is raised.
        
        Args:
            deposit (float): The amount to deposit into the account. Must be a 
                             positive number.
        
        Returns:
            float: The new account balance after the deposit.
        
        Raises:
            ValueError: If the customer ID is not found in the database.
            ValueError: If the deposit amount is not positive.
        
        Examples:
            >>> account = AccountTransactions('1001')
            >>> account.deposit(100.50)
            Deposited $100.50
            $600.50
            600.5
        """





cust_id = '1001'
account_transactions = AccountTransactions(cust_id)

try:
    account_transactions.balance()
except ValueError as e:
    print(f'Error: {e}')