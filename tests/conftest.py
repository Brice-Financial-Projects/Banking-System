"""Pytest fixtures for testing the banking system."""

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
