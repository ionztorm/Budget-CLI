import unittest

from budget.db import (
    DB_PATH,
    get_connection,
    create_data_path,
)


class TestDatabaseSetup(unittest.TestCase):
    def test_data_directory_exists(self) -> None:
        create_data_path()
        self.assertTrue(
            (DB_PATH.parent).exists(), "Data directory should exist"
        )

    def test_database_file_created(self) -> None:
        create_data_path()
        conn = get_connection()
        conn.close()
        self.assertTrue(
            DB_PATH.exists(), "Database file should exist after connection"
        )

    def test_required_tables_exist(self) -> None:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = {row[0] for row in cursor.fetchall()}
        conn.close()

        expected_tables = {"accounts", "subscriptions", "bills", "transactions"}
        for table in expected_tables:
            self.assertIn(table, tables, f"Table '{table}' should exist")


if __name__ == "__main__":
    unittest.main()
