# 🏦 Banking System (Python OOP Project)

This project is a modular, object-oriented simulation of a simple banking system. It was designed to reinforce Python fundamentals — including class structure, method design, exception handling, and in-memory data management — without relying heavily on AI code generation.

---

## 🚀 Features

- Create and close user accounts
- Store account data in an in-memory dictionary (`accounts_db`)
- Deposit and withdraw funds with balance tracking
- Raise custom `OverdraftError` if withdrawal exceeds balance
- Clean class separation between:
  - `BankAccount` (lifecycle management)
  - `BankTransactions` (fund movement)
- Prepares for future database integration (PostgreSQL planned)

---

## 🎯 Learning Objectives

This project was built to:

- Practice object-oriented design using Python classes and methods
- Simulate real-world system behavior without external dependencies
- Build confidence in manual coding (minimal AI/tool assistance)
- Set the foundation for future enhancements (REST API, user auth, etc.)

---

## 🛠️ Tech Stack

- Python 3.12
- Standard library only
- Virtual environment (`python -m venv venv`)
- Git for version control

---

## 📁 Project Structure

banking-system/
│
├── model/
│   ├── __init__.py
│   ├── account.py
│   ├── customer.py
│   ├── loan.py
│   └── account_activity.py
│
├── service/
│   ├── __init__.py
│   └── account_service.py
│
├── db/
│   ├── __init__.py
│   └── accounts_store.py
│
├── tests/
│   ├── __init__.py
│   └── test_account.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── venv/


---

## 🧭 Future Enhancements

- ✅ Add unit tests with `pytest`
- 🔜 Replace in-memory store with PostgreSQL
- 🔜 Expose account operations via Flask REST API
- 🔜 Add user authentication and session management

---

## 🧠 About This Project

This project is part of my transition from civil engineering into software and fintech. My goal is to showcase strong backend fundamentals while building systems that can scale.

> All code was written manually, without AI-assisted generation. AI tools were used only for review feedback and code critique.

---

## 🙌 Let's Connect

If you're interested in how I’m applying engineering discipline to fintech systems, feel free to follow my journey or reach out!

