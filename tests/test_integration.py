"""Integration tests for the banking system."""

import pytest
from unittest import mock

@pytest.fixture
def BankAccount():
    """Import and return the BankAccount class."""
    with mock.patch('model.account.accounts_db', {}):
        with mock.patch('builtins.print'):
            from model.account import BankAccount as BA
            return BA

@pytest.fixture
def AccountTransactions():
    """Import and return the AccountTransactions class."""
    with mock.patch('model.transactions.transactions_db', {}):
        with mock.patch('builtins.print'):
            from model.transactions import AccountTransactions as AT
            return AT


@pytest.fixture
def mock_both_dbs():
    """Mock both databases for integration testing."""
    accounts_mock = {}
    transactions_mock = {}

    with mock.patch('model.account.accounts_db', accounts_mock):
        with mock.patch('model.transactions.transactions_db', transactions_mock):
            yield accounts_mock, transactions_mock


def test_full_customer_workflow(mock_both_dbs, BankAccount, AccountTransactions):
    """Test the full customer workflow from account creation to transactions."""
    accounts_db, transactions_db = mock_both_dbs

    # Step 1: Create a bank account
    bank_account = BankAccount("Jane", "Doe")

    # Step 2: Create customer ID
    with mock.patch('builtins.print'):
        cust_id = bank_account.create_cust_id(
            "Jane", "Doe", "456 Oak St", "Springfield", "IL", "54321"
        )

    # Verify customer was created
    assert cust_id == 1001  # First customer should be 1001
    assert str(cust_id) in accounts_db or cust_id in accounts_db

    # Step 3: Set up transactions for this customer
    transactions_db[str(cust_id)] = {
        'deposit': [],
        'withdraw': [],
        'balance': 0.00
    }

    # Step 4: Create account transactions object
    account = AccountTransactions(str(cust_id))

    # Step 5: Perform transactions
    with mock.patch('builtins.print'):
        # Initial deposit
        account.deposit(500.00)

        # Check balance
        balance = account.balance()
        assert balance == 500.00

        # Make a withdrawal
        account.withdraw(150.00)

        # Check final balance
        final_balance = account.balance()
        assert final_balance == 350.00


def test_edge_case_account_creation_with_existing_number(mock_both_dbs, BankAccount):
    """Test account creation when a generated account number already exists."""
    accounts_db, _ = mock_both_dbs

    # Step 1: Create a bank account
    bank_account = BankAccount("Test", "User")

    # Step 2: Add an existing account with a known account number
    accounts_db['1001'] = {
        'first_name': 'existing',
        'last_name': 'user',
        'acct_num': '123456789012'
    }

    # Step 3: Mock random to first return the existing account number, then a new one
    with mock.patch('random.randint', side_effect=[1,2,3,4,5,6,7,8,9,0,1,2, 9,8,7,6,5,4,3,2,1,0,9,8]):
        # This should create an account with number '987654321098' after detecting '123456789012' exists
        account_num = bank_account.create_account("Test", "User")

        assert account_num != '123456789012'
        assert len(account_num) == 12
        assert account_num.isdigit()


def test_overdraft_scenario(mock_both_dbs, AccountTransactions):
    """Test withdrawing more than the balance."""
    _, transactions_db = mock_both_dbs

    # Set up an account with a balance
    transactions_db['1001'] = {
        'deposit': [100.00],
        'withdraw': [],
        'balance': 100.00
    }

    account = AccountTransactions('1001')

    with mock.patch('builtins.print'):
        # Current implementation allows overdraft
        new_balance = account.withdraw(150.00)

        # Check that balance went negative
        assert new_balance == -50.00
        assert transactions_db['1001']['balance'] == -50.00


def test_multiple_customer_accounts(mock_both_dbs, BankAccount, AccountTransactions):
    """Test creating and managing multiple customer accounts."""
    accounts_db, transactions_db = mock_both_dbs

    # Create two bank accounts
    bank_account1 = BankAccount("Alice", "Smith")
    bank_account2 = BankAccount("Bob", "Jones")

    # Create customer IDs
    with mock.patch('builtins.print'):
        with mock.patch.object(bank_account1, 'create_account', side_effect=['111111111111', '222222222222']):
            cust_id1 = bank_account1.create_cust_id(
                "Alice", "Smith", "789 Pine St", "Boston", "MA", "02101"
            )
            cust_id2 = bank_account2.create_cust_id(
                "Bob", "Jones", "321 Maple Ave", "Chicago", "IL", "60601"
            )

    # Set up transactions for both customers
    transactions_db[str(cust_id1)] = {
        'deposit': [],
        'withdraw': [],
        'balance': 0.00
    }

    transactions_db[str(cust_id2)] = {
        'deposit': [],
        'withdraw': [],
        'balance': 0.00
    }

    # Create transaction objects
    account1 = AccountTransactions(str(cust_id1))
    account2 = AccountTransactions(str(cust_id2))

    # Perform different transactions for each account
    with mock.patch('builtins.print'):
        account1.deposit(1000.00)
        account2.deposit(500.00)

        account1.withdraw(200.00)
        account2.withdraw(100.00)

        # Check balances are tracked separately
        balance1 = account1.balance()
        balance2 = account2.balance()

        assert balance1 == 800.00
        assert balance2 == 400.00

        # Additional operations
        account1.deposit(50.00)
        account2.withdraw(50.00)

        # Final balances
        final_balance1 = account1.balance()
        final_balance2 = account2.balance()

        assert final_balance1 == 850.00
        assert final_balance2 == 350.00
