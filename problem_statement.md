# 🧠 AI-Free Python Practice Challenges

Welcome, brave dev! The following exercises are designed to help you strengthen your coding fluency without AI assistance. Treat these like mini-interviews or warm-ups before your coding workouts.

---

## 🧾 Challenge 1: Bank Account Class

**Problem Statement**  
Create a class called `BankAccount` with the following features:

- A constructor that takes `owner_name` and an optional `starting_balance` (default to 0).
- A `deposit(amount)` method that adds money to the balance.
- A `withdraw(amount)` method that subtracts money from the balance, unless it would go negative.
- A `get_balance()` method that returns the current balance.

**Bonus**: Raise a custom `OverdraftError` if the user tries to withdraw more than the balance.

---

## 🧮 Challenge 2: CLI Average Calculator

**Problem Statement**  
Write a command-line Python program that:

1. Prompts the user to enter 5 numbers (you can use `input()` in a loop).
2. Stores the numbers in a list.
3. Calculates and prints the average of the numbers to 2 decimal places.

**Bonus**: Add error handling so the user must enter a valid number.

---

## 🌐 Challenge 3: Simple Flask REST API

**Problem Statement**  
Create a Flask API with the following endpoint:

- `GET /hello`: Returns a JSON response like `{"message": "Hello, world!"}`.

**Bonus**:
- Add a second endpoint: `POST /echo` that accepts a JSON payload like `{"data": "Test"}` and returns `{"you_sent": "Test"}`.
- Add error handling if no data is sent.

---

## 💡 Reminder

Try to complete these challenges without AI assistance.
- Use official Python docs: https://docs.python.org/3/
- Use print statements to debug if needed
- Write clean, readable code

When you’re done, review your work and try rewriting one from memory in 24 hours.

You’ve got this 💪
