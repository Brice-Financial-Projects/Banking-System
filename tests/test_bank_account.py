"""Tests for the BankAccount class."""

import pytest
import random
from unittest import mock

# We're using mock imports to avoid the auto-running code in the modules
@pytest.fixture
def BankAccount():
    """Import and return the BankAccount class."""
    with mock.patch('model.account.accounts_db', {}):
        with mock.patch('builtins.print'):
            from model.account import BankAccount as BA
            return BA

@pytest.fixture
def mock_accounts_db():
    """Fixture to create a mock accounts database."""
    with mock.patch('model.account.accounts_db', {}) as mock_db:
        yield mock_db

@pytest.fixture
def bank_account(BankAccount):
    """Fixture to create a BankAccount instance."""
    return BankAccount("Test", "User")


    def test_bank_account_initialization(BankAccount):
    """Test BankAccount initialization."""
    account = BankAccount("John", "Doe")
    assert account.first_name == "John"
    assert account.last_name == "Doe"


def test_create_account_generates_unique_account_number(bank_account):
    """Test that create_account generates a unique 12-digit account number."""
    # Call create_account method
    account_number = bank_account.create_account("Test", "User")

    # Verify account number format
    assert len(account_number) == 12
    assert account_number.isdigit()

    # Call it again to ensure uniqueness
    second_account_number = bank_account.create_account("Test", "User")
    assert account_number != second_account_number


def test_create_account_recursion_on_duplicate(bank_account):
    """Test that create_account recursively generates a new account number if a duplicate is found."""
    # Mock the random.randint to always return the same sequence
    with mock.patch('random.randint', side_effect=[1] * 12 + [2] * 12):
        # Add an account with the expected first account number
        mock_existing_account = {'acct_num': '111111111111'}

        # Use a context manager to simulate the account existing in the database
        with mock.patch('model.account.accounts_db.values', return_value=[mock_existing_account]):
            account_number = bank_account.create_account("Test", "User")

            # The function should have recursed and generated a different account number
            assert account_number == '222222222222'


def test_check_for_account_existing_customer(bank_account, mock_accounts_db):
    """Test check_for_account when the customer exists."""
    # Set up mock data
    mock_accounts_db['1001'] = {
        'first_name': 'John',
        'last_name': 'Doe',
        'acct_num': '123456789012'
    }

    # Test with existing customer
    with mock.patch('builtins.print') as mock_print:
        result = bank_account.check_for_account("John", "Doe")
        assert result is True
        mock_print.assert_called_with('John Doe already exists in the database.')


def test_check_for_account_new_customer(bank_account, mock_accounts_db):
    """Test check_for_account when the customer doesn't exist."""
    # Empty mock database
    with mock.patch('builtins.print') as mock_print:
        result = bank_account.check_for_account("Jane", "Smith")
        assert result is False
        mock_print.assert_called_with('Jane Smith does not exist in the database, needs a new account setup.\nRun create_cust_id')


def test_create_cust_id_new_customer(bank_account, mock_accounts_db):
    """Test create_cust_id for a new customer."""
    # Mock the check_for_account to return False (new customer)
    with mock.patch.object(bank_account, 'check_for_account', return_value=False):
        # Mock create_account to return a fixed account number
        with mock.patch.object(bank_account, 'create_account', return_value='123456789012'):
            # Test creating a new customer ID
            result = bank_account.create_cust_id("Jane", "Smith", "123 Main St", "Anytown", "CA", "12345")

            # Verify the result and the database update
            assert result == 1001  # Starting ID should be 1001 for empty database
            assert '1001' in mock_accounts_db or 1001 in mock_accounts_db

            # Get the entry regardless of whether the key is string or int
            entry = mock_accounts_db.get('1001', mock_accounts_db.get(1001))
            assert entry['first_name'] == "Jane"
            assert entry['last_name'] == "Smith"
            assert entry['acct_num'] == "123456789012"


def test_create_cust_id_existing_customer(bank_account, mock_accounts_db):
    """Test create_cust_id for an existing customer."""
    # Mock the check_for_account to return True (existing customer)
    with mock.patch.object(bank_account, 'check_for_account', return_value=True):
        with mock.patch('builtins.print') as mock_print:
            result = bank_account.create_cust_id("John", "Doe", "123 Main St", "Anytown", "CA", "12345")

            # Verify the result
            assert result is None
            mock_print.assert_called_with("Customer John Doe already exists. Skipping account creation.")


def test_create_cust_id_increments_id(bank_account, mock_accounts_db):
    """Test that create_cust_id increments the customer ID correctly."""
    # Add an existing customer with ID 1005
    mock_accounts_db[1005] = {
        'first_name': 'John',
        'last_name': 'Doe',
        'acct_num': '123456789012'
    }

    # Mock the check_for_account to return False (new customer)
    with mock.patch.object(bank_account, 'check_for_account', return_value=False):
        # Mock create_account to return a fixed account number
        with mock.patch.object(bank_account, 'create_account', return_value='987654321098'):
            # Test creating a new customer ID
            result = bank_account.create_cust_id("Jane", "Smith", "123 Main St", "Anytown", "CA", "12345")

            # Verify the result
            assert result == 1006  # Should increment from the highest existing ID (1005)


# Edge Cases
def test_create_cust_id_with_special_characters(bank_account, mock_accounts_db):
    """Test create_cust_id with special characters in names."""
    with mock.patch.object(bank_account, 'check_for_account', return_value=False):
        with mock.patch.object(bank_account, 'create_account', return_value='123456789012'):
            # Test with special characters in name
            result = bank_account.create_cust_id("O'Reilly", "Smith-Jones", "123 Main St", "Anytown", "CA", "12345")

            # Verify the result
            assert result == 1001

            # Get the entry regardless of whether the key is string or int
            entry = mock_accounts_db.get('1001', mock_accounts_db.get(1001))
            assert entry['first_name'] == "O'Reilly"
            assert entry['last_name'] == "Smith-Jones"
