"""Tests for overdraft scenarios with a custom OverdraftError."""

import pytest
from unittest import mock


# Since the BankAccount implementation doesn't yet have OverdraftError implemented
# We'll create tests that demonstrate how it should work

class OverdraftError(Exception):
    """Custom error for overdraft attempts."""
    pass


@pytest.fixture
def enhanced_account_transactions():
    """Mock an enhanced version of AccountTransactions with overdraft protection."""
    class EnhancedAccountTransactions:
        def __init__(self, cust_id):
            self.cust_id = cust_id
            # Mock transactions database
            self.transactions_db = {
                '1001': {
                    'deposit': [100.00],
                    'withdraw': [],
                    'balance': 100.00
                }
            }

        def balance(self):
            if self.cust_id in self.transactions_db:
                return self.transactions_db[self.cust_id]['balance']
            else:
                raise ValueError(f"Customer ID {self.cust_id} not found")

        def withdraw(self, amount):
            if amount <= 0:
                raise ValueError("Withdraw amount must be positive.")

            if self.cust_id not in self.transactions_db:
                raise ValueError("Customer ID not found.")

            current_balance = self.transactions_db[self.cust_id]['balance']

            # Check for overdraft
            if amount > current_balance:
                raise OverdraftError(f"Insufficient funds: Cannot withdraw ${amount:.2f} from balance of ${current_balance:.2f}")

            self.transactions_db[self.cust_id]['balance'] -= amount
            return self.transactions_db[self.cust_id]['balance']

    return EnhancedAccountTransactions('1001')


def test_withdraw_with_overdraft_protection(enhanced_account_transactions):
    """Test that withdrawing more than the balance raises OverdraftError."""
    # Current balance is 100.00

    # Withdraw an amount equal to balance should work
    new_balance = enhanced_account_transactions.withdraw(100.00)
    assert new_balance == 0.00

    # Reset balance for next test
    enhanced_account_transactions.transactions_db['1001']['balance'] = 100.00

    # Withdraw more than balance should raise OverdraftError
    with pytest.raises(OverdraftError) as excinfo:
        enhanced_account_transactions.withdraw(150.00)

    assert "Insufficient funds" in str(excinfo.value)

    # Balance should remain unchanged after failed withdrawal
    assert enhanced_account_transactions.balance() == 100.00


def test_withdraw_edge_amounts(enhanced_account_transactions):
    """Test withdrawals with edge case amounts."""
    # Withdraw exactly the balance
    new_balance = enhanced_account_transactions.withdraw(100.00)
    assert new_balance == 0.00

    # Reset balance
    enhanced_account_transactions.transactions_db['1001']['balance'] = 100.00

    # Withdraw just under the balance
    new_balance = enhanced_account_transactions.withdraw(99.99)
    assert new_balance == 0.01

    # Reset balance
    enhanced_account_transactions.transactions_db['1001']['balance'] = 100.00

    # Withdraw just over the balance
    with pytest.raises(OverdraftError) as excinfo:
        enhanced_account_transactions.withdraw(100.01)

    assert "Insufficient funds" in str(excinfo.value)
    assert enhanced_account_transactions.balance() == 100.00


def test_suggested_overdraft_implementation():
    """Demonstrates how the BankAccount withdraw method should be implemented with overdraft protection."""
    # This is a demonstration of the suggested implementation
    def withdraw_with_protection(balance, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        if amount > balance:
            raise OverdraftError(f"Insufficient funds: Cannot withdraw ${amount:.2f} from balance of ${balance:.2f}")

        return balance - amount

    # Test cases
    # Normal withdrawal
    assert withdraw_with_protection(100.00, 50.00) == 50.00

    # Edge case: withdraw exact balance
    assert withdraw_with_protection(100.00, 100.00) == 0.00

    # Overdraft attempt
    with pytest.raises(OverdraftError) as excinfo:
        withdraw_with_protection(100.00, 150.00)

    assert "Insufficient funds" in str(excinfo.value)

    # Invalid amount
    with pytest.raises(ValueError) as excinfo:
        withdraw_with_protection(100.00, -50.00)

    assert "must be positive" in str(excinfo.value)
