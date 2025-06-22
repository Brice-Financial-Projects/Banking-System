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
        """
        if deposit <= 0:
            raise ValueError("Deposit amount must be positive.")

        if self.cust_id not in transactions_db:
            raise ValueError("Customer ID not found.")

        transactions_db[self.cust_id]['balance'] += deposit

        new_balance = transactions_db[self.cust_id]['balance']
        print(f"Deposited ${deposit:.2f}")
        print(f"${new_balance:.2f}")

        return new_balance

    def withdraw(self, withdraw):
        """
        Withdraw funds from the customer's account.

        This method subtracts the specified amount from the customer's current balance
        in the transaction database. If the customer ID does not exist in the
        database, a ValueError is raised.

        Args:
            withdraw (float): The amount to withdraw from the account. Must be a
                             positive number.

        Returns:
            float: The new account balance after the withdraw.

        Raises:
            ValueError: If the customer ID is not found in the database.
            ValueError: If the withdraw amount is not positive.
        """
        if withdraw <= 0:
            raise ValueError('Withdraw amount must be positive.')

        if self.cust_id not in transactions_db:
            raise ValueError("Customer ID not found.")

        transactions_db[self.cust_id]['balance'] -= withdraw

        new_balance = transactions_db[self.cust_id]['balance']
        print(f"Withdraw ${withdraw:.2f}")
        print(f"${new_balance:.2f}")
        return new_balance

# Test code moved to a main block to prevent it from running when imported
if __name__ == "__main__":
    cust_id = '1001'
    account_transactions = AccountTransactions(cust_id)

    try:
        account_transactions.balance()
    except ValueError as e:
        print(f'Error: {e}')
