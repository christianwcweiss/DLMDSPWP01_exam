# pylint: disable=C0114  # noqa: D100
import os
from logging import getLogger
from typing import List

from sqlalchemy import Column  # type: ignore
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table  # type: ignore
from sqlalchemy.engine import Engine  # type: ignore

LOG = getLogger(__file__)


class SQLDatabase:
    """SQLite Database implementation."""

    def __init__(self) -> None:
        """Initialize a database. Output directory is fixed."""
        self._db_directory = os.path.join(os.getcwd(), "output")
        if not os.path.exists(self._db_directory):
            os.makedirs(self._db_directory)

        if not os.path.exists(f"{self._db_directory}/database.db"):
            open(f"{self._db_directory}/database.db", "w+", encoding="utf-8").close()  # pylint: disable=R1732

        self._engine = create_engine(f"sqlite:////{self._db_directory}/database.db")

    @property
    def engine(self) -> Engine:
        """Return the database engine."""
        return self._engine

    def create_table(self, table_name: str, columns: List[Column]) -> None:
        """Create a table in the database."""
        meta = MetaData()
        table = Table(table_name, meta, *columns)
        try:
            meta.create_all(self.engine, tables=[table], checkfirst=True)
        except AttributeError as error:
            LOG.error(f"Cannot create table due to the following error: {error}")  # pylint: disable=W1203

    def insert_into_table(self, table_name: str, column_names: List[Column], values: List[str]) -> None:
        """Insert a variable into the table."""
        parsed_names = ", ".join([column.name for column in column_names])
        parsed_values = ", ".join(values)

        with self.engine.connect() as connection:
            connection.execute(f"INSERT INTO {table_name} ({parsed_names}) " f"VALUES ({parsed_values})")

    def truncate_table(self, table_name: str) -> None:
        """Truncate a table."""
        with self.engine.connect() as connection:
            connection.execute(f"DELETE FROM {table_name}")
