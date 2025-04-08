CREATE_ACCOUNTS_TABLE = """
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY,
    provider_name TEXT NOT NULL,
    credit_limit REAL,
    statement_date TEXT,
    start_date TEXT,
    opening_balance REAL,
    interest_rate REAL
)
"""

CREATE_SUBSCRIPTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS subscriptions (
    id INTEGER PRIMARY KEY,
    service_name TEXT NOT NULL,
    pay_amount REAL NOT NULL
)
"""

CREATE_BILLS_TABLE = """
CREATE TABLE IF NOT EXISTS bills (
    id INTEGER PRIMARY KEY,
    bill_name TEXT NOT NULL,
    bill_date TEXT,
    payment_cycle TEXT,
    bill_amount REAL NOT NULL
)
"""

CREATE_TRANSACTIONS_TABLE = """
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    type TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT NOT NULL,
    spend_type TEXT NOT NULL,
    vendor_or_debtor_name TEXT NOT NULL,

    paid_from_account_id INTEGER,
    paid_to_account_id INTEGER,

    FOREIGN KEY (paid_from_account_id) REFERENCES accounts(id),
    FOREIGN KEY (paid_to_account_id) REFERENCES accounts(id)
)
"""
