"""Tests for the AccountTransactions class."""

import pytest
from unittest import mock

@pytest.fixture
def AccountTransactions():
    """Import and return the AccountTransactions class."""
    with mock.patch('model.transactions.transactions_db', {}):
        with mock.patch('builtins.print'):
            from model.transactions import AccountTransactions as AT
            return AT

@pytest.fixture
def mock_transactions_db():
    """Fixture to create a mock transactions database."""
    with mock.patch('model.transactions.transactions_db', {}) as mock_db:
        yield mock_db

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


def test_account_transactions_initialization(AccountTransactions):
    """Test AccountTransactions initialization."""
    account = AccountTransactions("1001")
    assert account.cust_id == "1001"


def test_balance_existing_account(setup_account_with_balance):
    """Test balance method with an existing account."""
    account, _ = setup_account_with_balance

    with mock.patch('builtins.print') as mock_print:
        balance = account.balance()
        assert balance == 75.00
        mock_print.assert_called_with('$75.0')


def test_balance_nonexistent_account(mock_transactions_db, AccountTransactions):
    """Test balance method with a non-existent account."""
    account = AccountTransactions("9999")

    with pytest.raises(ValueError) as excinfo:
        account.balance()

    assert "Customer ID 9999 not found in the database" in str(excinfo.value)


def test_deposit_valid_amount(setup_account_with_balance):
    """Test deposit with a valid amount."""
    account, mock_db = setup_account_with_balance

    with mock.patch('builtins.print') as mock_print:
        new_balance = account.deposit(50.00)

        # Check if the balance was updated correctly
        assert new_balance == 125.00
        assert mock_db['1001']['balance'] == 125.00

        # Check print statements
        mock_print.assert_any_call("Deposited $50.00")
        mock_print.assert_any_call("$125.00")


def test_deposit_negative_amount(setup_account_with_balance):
    """Test deposit with a negative amount."""
    account, mock_db = setup_account_with_balance

    with pytest.raises(ValueError) as excinfo:
        account.deposit(-50.00)

    assert "Deposit amount must be positive" in str(excinfo.value)
    # Ensure balance wasn't changed
    assert mock_db['1001']['balance'] == 75.00


def test_deposit_zero_amount(setup_account_with_balance):
    """Test deposit with zero amount."""
    account, mock_db = setup_account_with_balance

    with pytest.raises(ValueError) as excinfo:
        account.deposit(0.00)

    assert "Deposit amount must be positive" in str(excinfo.value)
    # Ensure balance wasn't changed
    assert mock_db['1001']['balance'] == 75.00


def test_deposit_to_nonexistent_account(mock_transactions_db, AccountTransactions):
    """Test deposit to a non-existent account."""
    account = AccountTransactions("9999")

    with pytest.raises(ValueError) as excinfo:
        account.deposit(50.00)

    assert "Customer ID not found" in str(excinfo.value)


def test_withdraw_valid_amount(setup_account_with_balance):
    """Test withdraw with a valid amount."""
    account, mock_db = setup_account_with_balance

    with mock.patch('builtins.print') as mock_print:
        new_balance = account.withdraw(25.00)

        # Check if the balance was updated correctly
        assert new_balance == 50.00
        assert mock_db['1001']['balance'] == 50.00

        # Check print statements
        mock_print.assert_any_call("Withdraw $25.00")
        mock_print.assert_any_call("$50.00")


def test_withdraw_negative_amount(setup_account_with_balance):
    """Test withdraw with a negative amount."""
    account, mock_db = setup_account_with_balance

    with pytest.raises(ValueError) as excinfo:
        account.withdraw(-25.00)

    assert "Withdraw amount must be positive" in str(excinfo.value)
    # Ensure balance wasn't changed
    assert mock_db['1001']['balance'] == 75.00


def test_withdraw_zero_amount(setup_account_with_balance):
    """Test withdraw with zero amount."""
    account, mock_db = setup_account_with_balance

    with pytest.raises(ValueError) as excinfo:
        account.withdraw(0.00)

    assert "Withdraw amount must be positive" in str(excinfo.value)
    # Ensure balance wasn't changed
    assert mock_db['1001']['balance'] == 75.00


def test_withdraw_from_nonexistent_account(mock_transactions_db, AccountTransactions):
    """Test withdraw from a non-existent account."""
    account = AccountTransactions("9999")

    with pytest.raises(ValueError) as excinfo:
        account.withdraw(25.00)

    assert "Customer ID not found" in str(excinfo.value)


# Edge cases
def test_withdraw_entire_balance(setup_account_with_balance):
    """Test withdrawing the entire balance."""
    account, mock_db = setup_account_with_balance

    with mock.patch('builtins.print') as mock_print:
        new_balance = account.withdraw(75.00)

        # Check if the balance was updated correctly
        assert new_balance == 0.00
        assert mock_db['1001']['balance'] == 0.00


def test_withdraw_more_than_balance(setup_account_with_balance):
    """Test withdrawing more than the balance."""
    account, mock_db = setup_account_with_balance

    with mock.patch('builtins.print') as mock_print:
        # The current implementation allows overdraft
        new_balance = account.withdraw(100.00)

        # Check if the balance was updated correctly (negative balance)
        assert new_balance == -25.00
        assert mock_db['1001']['balance'] == -25.00


def test_deposit_very_large_amount(setup_account_with_balance):
    """Test depositing a very large amount."""
    account, mock_db = setup_account_with_balance
    large_amount = 1000000000.00  # 1 billion

    with mock.patch('builtins.print') as mock_print:
        new_balance = account.deposit(large_amount)

        # Check if the balance was updated correctly
        assert new_balance == 75.00 + large_amount
        assert mock_db['1001']['balance'] == 75.00 + large_amount


def test_multiple_operations(setup_account_with_balance):
    """Test multiple operations in sequence."""
    account, mock_db = setup_account_with_balance

    with mock.patch('builtins.print'):
        # Perform multiple operations
        account.deposit(100.00)    # 75 + 100 = 175
        account.withdraw(50.00)    # 175 - 50 = 125
        account.deposit(25.00)     # 125 + 25 = 150
        final_balance = account.withdraw(30.00)  # 150 - 30 = 120

        # Check final balance
        assert final_balance == 120.00
        assert mock_db['1001']['balance'] == 120.00
