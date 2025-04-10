"""
Accounts Model

This module defines the Accounts class used to interact with the 'accounts'
table in the SQLite database. It inherits from the Tables base class, and
provides methods for CRUD operations: retrieving one or all records,
inserting new data, editing existing entries, and deleting rows.
"""

import sqlite3

from typing import TYPE_CHECKING, override

from budget.models.base import Tables

if TYPE_CHECKING:
    from budget.models.constants import TableName


class Accounts(Tables):
    """
    Model class for interacting with the 'accounts' table in the database.
    Provides methods to retrieve, insert, update, and delete account records.
    """

    def __init__(self, conn: sqlite3.Connection) -> None:
        """
        Initialise the Accounts model with a database connection.

        Args:
            conn (sqlite3.Connection): An active SQLite connection.
        """
        super().__init__(conn)
        self._table_name: TableName = "accounts"

    @override
    def get(self, id: int) -> dict | None:
        """
        Retrieve a single account by its ID.

        Args:
            id (int): The ID of the account to retrieve.

        Returns:
            None: To be implemented.
        """
        self._cursor.execute(
            f"SELECT * FROM {self._table_name} WHERE id = ?",  # noqa: S608
            (id,),
        )
        row = self._cursor.fetchone()
        return self.row_to_dict(row) if row else None

    @override
    def get_all(self) -> list:
        """
        Retrieve all account records from the database.

        Returns:
            list: A list of dictionaries, each representing an account record.
        """
        self._cursor.execute(f"SELECT * FROM {self._table_name}")  # noqa: S608
        rows = self._cursor.fetchall()
        return [self.row_to_dict(row) for row in rows]

    @override
    def add(self, data: dict) -> None:
        """
        Add a new account to the database.

        Args:
            data (dict): A dictionary containing account data to insert.

        Returns:
            None: To be implemented.
        """
        self._cursor.execute(f"PRAGMA table_info({self._table_name})")
        columns = [row[1] for row in self._cursor.fetchall() if row[1] != "id"]

        placeholders = ", ".join("?" for _ in columns)
        col_list = ", ".join(columns)
        values = tuple(data.get(col) for col in columns)

        self._cursor.execute(
            f"INSERT INTO {self._table_name} "  # noqa: S608
            f"({col_list}) VALUES ({placeholders})",
            values,
        )
        self._conn.commit()

    @override
    def edit(self, id: int, data: dict) -> None:
        """
        Edit an existing account in the database.

        Args:
            id (int): The ID of the account to edit.
            data (dict): A dictionary of fields to update.

        Returns:
            None: To be implemented.
        """
        pass

    @override
    def delete(self, id: int) -> None:
        """
        Delete an account from the database by ID.

        Args:
            id (int): The ID of the account to delete.

        Returns:
            None: To be implemented.
        """
        pass
