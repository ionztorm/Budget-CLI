"""
Accounts Model

This module defines the Accounts class used to interact with the 'accounts'
table in the SQLite database. It inherits from the Tables base class, and
provides methods for CRUD operations: retrieving one or all records,
inserting new data, editing existing entries, and deleting rows.
"""

import sqlite3

from typing import override

from budget.models.base import Tables
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
        super().__init__(conn, TableName.ACCOUNTS)

    @override
    def get(self, id: int) -> None:
        """
        Retrieve a single account by its ID.

        Args:
            id (int): The ID of the account to retrieve.

        Returns:
            None: To be implemented.
        """
        pass

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
        pass

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
