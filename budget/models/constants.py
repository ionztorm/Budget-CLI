from enum import Enum


class TableName(str, Enum):
    ACCOUNTS = "accounts"
    BILLS = "bills"
    SUBSCRIPTIONS = "subscriptions"
    TRANSACTIONS = "transactions"
