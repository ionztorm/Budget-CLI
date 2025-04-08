import sqlite3

from pathlib import Path

from .schema import (
    CREATE_BILLS_TABLE,
    CREATE_ACCOUNTS_TABLE,
    CREATE_TRANSACTIONS_TABLE,
    CREATE_SUBSCRIPTIONS_TABLE,
)

ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
DB_PATH = DATA_DIR / "budget.db"


def create_data_path() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(CREATE_ACCOUNTS_TABLE)
    cursor.execute(CREATE_BILLS_TABLE)
    cursor.execute(CREATE_SUBSCRIPTIONS_TABLE)
    cursor.execute(CREATE_TRANSACTIONS_TABLE)
    conn.commit()
    return conn
