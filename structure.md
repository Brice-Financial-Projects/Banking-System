banking-system/
│
├── config/                      # 💼 Config Files - Configuration settings
│   ├── __init__.py              # Makes this a Python package
│   └── settings.py              # Defines the Config class 
│
├── model/                       # 💼 Domain Models - Core business entities
│   ├── __init__.py              # Makes this a Python package
│   ├── account.py               # Defines the BankAccount class (open/close, balance mgmt)
│   ├── customer.py              # Represents Customer entity (name, ID, contact, etc.)
│   ├── loan.py                  # Defines Loan class and loan-related logic
│   └── account_activity.py      # Tracks deposits, withdrawals, and other account actions
│
├── service/                     # 🧠 Business Logic Layer - Coordinates behavior using models
│   ├── __init__.py              # Package initializer
│   └── account_service.py       # Handles high-level operations (create account, transfer, etc.)
│
├── db/                          # 🗄️ In-memory or future persistent data layer
│   ├── __init__.py              # Package initializer
│   └── accounts_store.py        # Temporary in-memory data store (e.g., accounts_db dictionary)
│
├── tests/                       # 🧪 Unit Tests
│   ├── __init__.py              # Package initializer (optional for discovery)
│   └── test_account.py          # Tests for account functionality (using unittest or pytest)
│
├── README.md                    # 📘 Project overview, setup, and documentation
├── requirements.txt             # 📦 Dependency list (if any external libraries are used)
├── .gitignore                   # 🚫 Files/folders Git should ignore (e.g., venv, __pycache__)
└── venv/                        # 🐍 Local virtual environment (typically ignored in version control)

