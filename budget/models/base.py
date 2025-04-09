"""
Abstract base class for all SQL-backed data models.

Subclasses must implement standard CRUD operations.
"""

import sqlite3

from .constants import TableName


class Tables:
    def __init__(self, conn: sqlite3.Connection, table_name: TableName) -> None:
        """
        Initialise the table with a database connection.

        Args:
            conn (sqlite3.Connection): An active SQLite connection.
        """
        if not isinstance(table_name, TableName):
            raise TypeError("Expected table_name to be a TableName enum")
        self._conn = conn
        self._cursor = self._conn.cursor()
        self._table_name = table_name.value

    def get(self, id: int) -> dict | None:
        """
        Retrieve a single row by ID.

        Args:
            id (int): The ID of the record to retrieve.
        """
        raise NotImplementedError

    def get_all(self) -> list:
        """Retrieve all rows from the table."""
        raise NotImplementedError

    def add(self, data: dict) -> None:
        """
        Add a new row with the given data.

        Args:
            data (dict): A dictionary of column-value pairs to insert.
        """
        raise NotImplementedError

    def edit(self, id: int, data: dict) -> None:
        """
        Edit a row by ID using the new data.

        Args:
            id (int): The ID of the row to update.
            data (dict): Dictionary of updated column-value pairs.
        """
        raise NotImplementedError

    def delete(self, id: int) -> None:
        """
        Delete a row by ID.

        Args:
            id (int): The ID of the row to delete.
        """
        raise NotImplementedError

    def row_to_dict(self, row: sqlite3.Row) -> dict:
        """
        Convert a SQLite row object to a dictionary.

        Args:
            row (sqlite3.Row): A single row returned by cursor.fetchone()/
            fetchall()

        Returns:
            dict: A dictionary mapping column names to values.
        """
        return dict(
            zip(
                [column[0] for column in self._cursor.description],
                row,
                strict=False,
            )
        )

    def exists(self, id: int) -> bool:
        """
        Check if a record with the given ID exists in the table.

        Args:
            id (int): The ID to check.

        Returns:
            bool: True if the record exists, False otherwise.
        """
        self._cursor.execute(
            f"SELECT 1 FROM {self._table_name} WHERE id = ?",  # noqa: S608
            (id,),
        )
        return self._cursor.fetchone() is not None

    def count(self) -> int:
        """
        Count the number of rows in the table.

        Returns:
            int: The total number of records.
        """
        self._cursor.execute(f"SELECT COUNT(*) FROM {self._table_name}")  # noqa: S608

        return self._cursor.fetchone()[0]
