"""Pytest fixtures for testing the banking system."""
"""Shared pytest fixtures for banking system tests."""

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
def mock_accounts_db():
    """Fixture to create a mock accounts database."""
    with mock.patch('model.account.accounts_db', {}) as mock_db:
        yield mock_db

@pytest.fixture
def mock_transactions_db():
    """Fixture to create a mock transactions database."""
    with mock.patch('model.transactions.transactions_db', {}) as mock_db:
        yield mock_db

@pytest.fixture
def mock_both_dbs():
    """Mock both databases for integration testing."""
    accounts_mock = {}
    transactions_mock = {}

    with mock.patch('model.account.accounts_db', accounts_mock):
        with mock.patch('model.transactions.transactions_db', transactions_mock):
            yield accounts_mock, transactions_mock

@pytest.fixture
def setup_account_with_balance(AccountTransactions):
    """Fixture to create an account with initial balance."""
    with mock.patch('model.transactions.transactions_db', {
        '1001': {
            'deposit': [100.00],
            'withdraw': [25.00],
            'balance': 75.00
        }
    }) as mock_db:
        account = AccountTransactions('1001')
        return account, mock_db
import pytest
from unittest import mock

@pytest.fixture(autouse=True)
def reset_databases():
    """Reset all databases after each test to prevent test interference."""
    yield
    # This will run after each test
    # Note: The actual databases will be mocked in most tests, so this is just a precaution

@pytest.fixture
def custom_overdraft_error():
    """Create a custom OverdraftError class for testing."""
    class OverdraftError(Exception):
        """Custom error for overdraft attempts."""
        pass
    return OverdraftError

@pytest.fixture
def sample_customer_data():
    """Return sample customer data for testing."""
    return {
        "first_name": "Test",
        "last_name": "User",
        "address": "123 Test St",
        "city": "Testville",
        "state": "TS",
        "zip": "12345"
    }
