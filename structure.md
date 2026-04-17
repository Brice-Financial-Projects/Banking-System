banking-system/
│
├── src/
│   └── banking_system/          # Python package container (src layout)
│       ├── __init__.py
│       ├── config/
│       │   ├── __init__.py
│       │   └── settings.py
│       ├── db/
│       │   ├── __init__.py
│       │   └── accounts_store.py
│       └── model/
│           ├── __init__.py
│           ├── account.py
│           ├── overdraft.py
│           ├── pseudo_account.py
│           └── transactions.py
│
├── tests/                       # Unit tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_account_transactions.py
│   ├── test_bank_account.py
│   ├── test_custom_bank_account.py
│   ├── test_integration.py
│   └── test_overdraft.py
│
├── pyproject.toml               # Build and dependency configuration
├── requirements.txt             # Optional pinned requirements
├── README.md
└── structure.md

