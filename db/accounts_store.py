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
    }
}
"""


accounts_db = {
    '1001': {
    'first_name': 'briana',
    'last_name': 'smith',
    'acct_num': '854876552154',
    'address': '2780 briar cliff rd',
    'city': 'miami',
    'state': 'FL',
    'zip': 12345,
    }
}

transactions_db = {
    '1001': {
        'deposit':[50.00,80.24],
        'withdraw': [37.00, 21.52],
        'balance': 71.72
    }
}
