# Banking System Tests

This directory contains tests for the banking system, focusing on the `BankAccount` and `AccountTransactions` classes. The tests are written using pytest and cover both unit tests and integration tests.

## Test Files

- `test_bank_account.py`: Tests for the `BankAccount` class
- `test_account_transactions.py`: Tests for the `AccountTransactions` class
- `test_integration.py`: Integration tests for both classes working together
- `test_overdraft.py`: Tests for overdraft scenarios and demonstrates recommended implementation
- `conftest.py`: Shared pytest fixtures

## Running the Tests

To run the tests, you'll need pytest installed. You can install it using pip:

```bash
pip install pytest
```

Then run the tests from the project root:

```bash
python -m pytest tests/
```

Or to run a specific test file:

```bash
python -m pytest tests/test_bank_account.py
```

With verbose output:

```bash
python -m pytest -v tests/
```

## Test Coverage

These tests cover:

- Basic functionality of both classes
- Edge cases (e.g., withdrawing exactly the balance)
- Error cases (e.g., withdrawing more than the balance)
- Integration between account creation and transaction handling

## Notes on Mocking

The tests make extensive use of unittest.mock to isolate components and ensure tests don't interfere with each other.

## Recommendations

The `test_overdraft.py` file includes a recommended implementation for overdraft protection that isn't yet implemented in the current code. This demonstrates how the `withdraw` method could be enhanced to prevent overdrafts by raising a custom `OverdraftError`.
