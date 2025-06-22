"""Tests for an enhanced BankAccount class with overdraft protection."""

import pytest
from unittest import mock


class OverdraftError(Exception):
    """Custom error for overdraft attempts."""
    pass


@pytest.fixture
def EnhancedBankAccount():
    """Create an enhanced version of BankAccount with full functionality."""
    class EnhancedBankAccount:
        def __init__(self, owner_name, starting_balance=0):
            """Initialize with owner name and optional starting balance."""
            self.owner_name = owner_name
            self.balance = starting_balance

        def deposit(self, amount):
            """Add money to the balance."""
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")

            self.balance += amount
            return self.balance

        def withdraw(self, amount):
            """Subtract money from the balance unless it would go negative."""
            if amount <= 0:
                raise ValueError("Withdraw amount must be positive")

            if amount > self.balance:
                raise OverdraftError(f"Insufficient funds: Cannot withdraw ${amount:.2f} from balance of ${self.balance:.2f}")

            self.balance -= amount
            return self.balance

        def get_balance(self):
            """Return the current balance."""
            return self.balance

    return EnhancedBankAccount


def test_enhanced_bank_account_init(EnhancedBankAccount):
    """Test initialization with and without starting balance."""
    # Default balance
    account1 = EnhancedBankAccount("John Doe")
    assert account1.owner_name == "John Doe"
    assert account1.balance == 0

    # Custom starting balance
    account2 = EnhancedBankAccount("Jane Smith", 100.00)
    assert account2.owner_name == "Jane Smith"
    assert account2.balance == 100.00


def test_enhanced_deposit(EnhancedBankAccount):
    """Test deposit functionality."""
    account = EnhancedBankAccount("Test User", 50.00)

    # Valid deposit
    new_balance = account.deposit(25.00)
    assert new_balance == 75.00
    assert account.balance == 75.00

    # Another valid deposit
    new_balance = account.deposit(125.00)
    assert new_balance == 200.00
    assert account.balance == 200.00

    # Invalid deposits
    with pytest.raises(ValueError) as excinfo:
        account.deposit(0)
    assert "must be positive" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        account.deposit(-50.00)
    assert "must be positive" in str(excinfo.value)

    # Balance should be unchanged after failed deposits
    assert account.balance == 200.00


def test_enhanced_withdraw(EnhancedBankAccount):
    """Test withdraw functionality with overdraft protection."""
    account = EnhancedBankAccount("Test User", 100.00)

    # Valid withdrawal
    new_balance = account.withdraw(25.00)
    assert new_balance == 75.00
    assert account.balance == 75.00

    # Another valid withdrawal
    new_balance = account.withdraw(50.00)
    assert new_balance == 25.00
    assert account.balance == 25.00

    # Invalid withdrawals
    with pytest.raises(ValueError) as excinfo:
        account.withdraw(0)
    assert "must be positive" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        account.withdraw(-10.00)
    assert "must be positive" in str(excinfo.value)

    # Overdraft attempt
    with pytest.raises(OverdraftError) as excinfo:
        account.withdraw(30.00)  # Trying to withdraw more than balance (25.00)
    assert "Insufficient funds" in str(excinfo.value)

    # Balance should be unchanged after failed withdrawals
    assert account.balance == 25.00


def test_enhanced_get_balance(EnhancedBankAccount):
    """Test get_balance functionality."""
    account = EnhancedBankAccount("Test User", 75.50)

    # Initial balance
    assert account.get_balance() == 75.50

    # After deposit
    account.deposit(24.50)
    assert account.get_balance() == 100.00

    # After withdrawal
    account.withdraw(40.00)
    assert account.get_balance() == 60.00


def test_enhanced_edge_cases(EnhancedBankAccount):
    """Test edge cases for the enhanced bank account."""
    account = EnhancedBankAccount("Test User", 100.00)

    # Withdrawing exactly the balance amount
    new_balance = account.withdraw(100.00)
    assert new_balance == 0.00
    assert account.get_balance() == 0.00

    # Trying to withdraw from empty account
    with pytest.raises(OverdraftError) as excinfo:
        account.withdraw(0.01)
    assert "Insufficient funds" in str(excinfo.value)

    # Depositing to empty account
    new_balance = account.deposit(200.00)
    assert new_balance == 200.00

    # Float precision edge case
    account = EnhancedBankAccount("Test User", 100.10)
    new_balance = account.withdraw(100.09)
    assert new_balance == 0.01
    with pytest.raises(OverdraftError) as excinfo:
        account.withdraw(0.02)
    assert "Insufficient funds" in str(excinfo.value)


def test_enhanced_multiple_operations(EnhancedBankAccount):
    """Test a sequence of operations."""
    account = EnhancedBankAccount("Test User", 100.00)

    # Sequence of operations
    account.deposit(50.00)  # 100 + 50 = 150
    account.withdraw(30.00)  # 150 - 30 = 120
    account.deposit(10.00)  # 120 + 10 = 130
    account.withdraw(25.00)  # 130 - 25 = 105
    account.withdraw(75.00)  # 105 - 75 = 30
    account.deposit(70.00)  # 30 + 70 = 100

    assert account.get_balance() == 100.00

    # Try to overdraw
    with pytest.raises(OverdraftError):
        account.withdraw(100.01)

    # Final balance should be unchanged
    assert account.get_balance() == 100.00
