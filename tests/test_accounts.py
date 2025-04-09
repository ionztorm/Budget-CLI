import sqlite3
import unittest

from pathlib import Path

from budget.schema import CREATE_ACCOUNTS_TABLE
from budget.models.accounts import Accounts


class TestAccountsModel(unittest.TestCase):
    def setUp(self) -> None:
        test_dir = Path(__file__).parent / "data"
        test_dir.mkdir(parents=True, exist_ok=True)
        self.temp_path = test_dir / "temp.db"
        self.conn = sqlite3.connect(self.temp_path)
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.conn.execute(CREATE_ACCOUNTS_TABLE)
        self.conn.commit()
        self.model = Accounts(self.conn)

    def tearDown(self) -> None:
        self.conn.close()
        self.temp_path.unlink(missing_ok=True)

    def test_get_all_returns_inserted_account(self) -> None:
        # Insert a test account
        self.conn.execute(
            "INSERT INTO accounts (provider_name, credit_limit) VALUES (?, ?)",
            ("TestBank", 1234.56),
        )
        self.conn.commit()

        results = self.model.get_all()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["provider_name"], "TestBank")
        self.assertAlmostEqual(results[0]["credit_limit"], 1234.56)


if __name__ == "__main__":
    unittest.main()
