"""model/pseudo_account.py"""

def create_account(self, customer_name, email, initial_deposit=0.0):
    # Step 1: Generate customer ID
    customer_id = f"CUST{self.next_customer_id:04d}"  # padded like CUST0001
    self.next_customer_id += 1

    # Step 2: Create Customer object
    customer = Customer(customer_id=customer_id, name=customer_name, email=email)

    # Step 3: Generate random 12-digit account number
    while True:
        account_number = random.randint(10**11, 10**12 - 1)
        if account_number not in self.accounts_db:
            break

    # Step 4: Create BankAccount
    account = BankAccount(account_number=account_number, balance=initial_deposit)

    # Step 5: Store in dictionary
    self.accounts_db[account_number] = {
        "customer": customer,
        "account": account,
        "activity": []
    }

    return account_number
