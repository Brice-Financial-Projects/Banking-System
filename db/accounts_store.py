"""
db/accounts_store.py

accounts_db {
    cust_id: {
    first_name: fname,
    last_name: lname,
    acct_num: acct_num,
    address: address,
    city: city,
    state: state,
    zip: zip,
    }
}

transactions_db {
    cust_id: {
    deposits: [*args],
    withdrawals: [*args],
    balance: balance
"""


accounts_db = {}

transactions = {}
