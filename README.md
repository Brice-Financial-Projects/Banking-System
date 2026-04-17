# 🏦 Python Banking System for Fintech Applications

A modular, object-oriented Python backend system simulating real-world banking workflows. This project demonstrates the foundational components of a fintech-style architecture, including customer account creation, transaction handling, loan management, and activity logging — all using clean code principles and scalable design patterns.

Designed for Python backend engineering roles in the fintech space, this system emphasizes:

- Domain-driven modeling (`BankAccount`, `Customer`, `Loan`, `AccountActivity`)
- Layered architecture (`model/`, `service/`, `db/`)
- Exception handling with custom errors (e.g., `OverdraftError`)
- Readiness for integration into a REST API (Flask/FastAPI/Django-compatible)
- Environment-specific configuration support via `.env` and `settings.py` scaffolding

All functionality was developed **manually, without AI code generation**, to deepen language fluency and build production-ready coding habits.

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
- `.env` file (with `config/settings.py`) for environment variable-based app configuration

---

## 📁 Project Structure

```plaintext
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
├── .env                         # environment variables (Not included in version control)
├── env.example                 # example of environment variables (included in version control)
└── venv/                        # 🐍 Local virtual environment (typically ignored in version control)
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

This project is part of my transition from civil engineering to software engineering, with a focus on backend development for fintech applications.

It reflects my commitment to writing clean, extensible code — and building systems that mirror real-world financial infrastructure from the ground up.

> All code was written manually. AI was used solely for the README as well as for critique and review purposes.

---

## 🔖 Tags

`python` `banking system` `fintech` `object-oriented programming` `backend developer`  
`flask api` `account management` `transactions` `unit testing` `modular architecture`  
`python projects` `python backend` `software engineering portfolio` `transition to tech`

---

## 🙌 Let's Connect

If you're hiring for backend Python roles in fintech, or just want to follow my engineering journey, feel free to connect:

- 💼 [LinkedIn](https://www.linkedin.com/in/brice-a-nelson-p-e-mba-36b28b15/)
- 📂 [My GitHub Financial Projects Portfolio](https://github.com/Brice-Financial-Projects)
- ✍️ [Medium Blog](https://medium.com/@quantshift) 
