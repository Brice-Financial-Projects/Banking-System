# 🏦 Python Banking System for Fintech Applications

A modular, object-oriented Python backend system simulating real-world banking workflows. This project demonstrates the foundational components of a fintech-style architecture, including customer account creation, transaction handling, loan management, and activity logging — all using clean code principles and scalable design patterns.

Designed for Python backend engineering roles in the fintech space, this system emphasizes:

- Domain-driven modeling (`BankAccount`, `Customer`, `Loan`, `AccountActivity`)
- Layered architecture in a src layout (`src/banking_system/model`, `src/banking_system/db`, `src/banking_system/config`)
- Exception handling with custom errors (e.g., `OverdraftError`)
- Readiness for integration into a REST API (Flask/FastAPI/Django-compatible)
- Environment-specific configuration support via `.env` and `settings.py` scaffolding

All core banking functionality and business logic were developed **manually, without AI code generation**, to deepen language fluency and build production-ready coding habits.

---

## 🚀 Features

- ✅ Create and close user accounts
- ✅ Deposit and withdraw with balance validation
- ✅ Track loan objects and activity logs
- ✅ Raise custom exceptions for overdraft protection
- ✅ In-memory database (`accounts_db`) simulating future PostgreSQL implementation
- ✅ Clean OOP class separation for long-term extensibility
- ✅ `.env`-driven configuration setup to support development, testing, and production modes

---

## 🎯 Learning Objectives

This project reinforces key backend development skills relevant to fintech roles:

- Structuring scalable, testable Python systems
- Building full backend logic without frameworks or boilerplate
- Demonstrating code ownership without reliance on AI tools
- Laying the groundwork for full-stack or API-driven fintech apps

---

## 🛠️ Tech Stack

- Python 3.12
- Standard library only
- `python -m venv` for isolated environments
- Git/GitHub for version control and documentation
- `.env` file (with `src/banking_system/config/settings.py`) for environment variable-based app configuration

---

## 📁 Project Structure

```plaintext
banking-system/
│
├── src/                         # 📦 Source root for installable Python packages
│   └── banking_system/          # 🏦 Main application package container
│       ├── __init__.py          # Exposes banking_system as a Python package
│       ├── config/              # 💼 Configuration layer for environment-based settings
│       │   ├── __init__.py      # Makes config importable as a package
│       │   └── settings.py      # Defines Config, Development, Testing, and Production settings
│       ├── db/                  # 🗄️ In-memory data layer and persistence placeholders
│       │   ├── __init__.py      # Makes db importable as a package
│       │   └── accounts_store.py # Stores mock accounts_db and transactions_db dictionaries
│       └── model/               # 💼 Domain models and banking business objects
│           ├── __init__.py      # Makes model importable as a package
│           ├── account.py       # Defines the BankAccount class and customer account creation logic
│           ├── overdraft.py     # Defines the custom OverdraftError exception
│           ├── pseudo_account.py # Holds early pseudo-code or alternate account creation ideas
│           └── transactions.py  # Defines AccountTransactions for deposits, withdrawals, and balances
│
├── docs/                        # 📚 Project documentation and reference notes
│   └── structure.md             # Documents the current repository layout with explanations
│
├── tests/                       # 🧪 Test suite covering units, integration paths, and edge cases
│   ├── __init__.py              # Marks tests as a package for certain import/discovery cases
│   ├── conftest.py              # Shared pytest fixtures and reusable test setup helpers
│   ├── test_account_transactions.py # Verifies deposit, withdraw, and balance behavior
│   ├── test_bank_account.py     # Tests bank account creation and customer record behavior
│   ├── test_custom_bank_account.py # Explores enhanced or alternate bank account behavior
│   ├── test_integration.py      # Validates end-to-end workflows across account and transaction modules
│   └── test_overdraft.py        # Covers overdraft-related scenarios and expected error behavior
│
├── .env.example                 # 🧾 Example environment variables for local configuration
├── pyproject.toml               # ⚙️ Project metadata, dependencies, pytest, and setuptools config
├── requirements.txt             # 📦 Pinned dependency list for environments that still use pip requirements files
├── uv.lock                      # 🔒 Lockfile capturing fully resolved dependency versions
├── README.md                    # 📘 Project overview, setup, and architecture notes
├── .gitignore                   # 🚫 Files and folders Git should ignore
├── .venv/                       # 🐍 Local virtual environment directory (typically ignored)
├── .pytest_cache/               # 🧪 Pytest cache artifacts from local test runs
└── .coverage                    # 📊 Coverage data file generated by pytest-cov/coverage
```

---

## 🧭 Future Enhancements

- ✅ Unit testing with `pytest`
- 🔜 PostgreSQL integration to replace in-memory store
- 🔜 REST API via Flask, FastAPI, or Django
- 🔜 Authentication system with role-based permissions
- 🔜 Config class expansion to support dynamic toggling (Dev, Test, Prod)

---

## 🧠 About This Project

This project was built from scratch, without any AI code generation, to demonstrate my ability to architect and implement a complex backend system using clean code principles and OOP design patterns.

> Core business logic was written manually. AI assistance was limited to documentation, critique/review, and project-structure updates (for example, src-layout import and packaging configuration).

---

## 🙌 Let's Connect

If you’d like to connect or follow my engineering journey, feel free to reach out:

- 💼 [LinkedIn](https://www.linkedin.com/in/brice-a-nelson-p-e-mba-36b28b15/)
- 📂 [My GitHub Financial Projects Portfolio](https://github.com/Brice-Financial-Projects)
- ✍️ [Medium Blog](https://medium.com/@quantshift) 
