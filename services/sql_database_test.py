# pylint: disable=C0114  # noqa: D100
import os
import tempfile
from typing import AnyStr
from unittest.mock import Mock

import pytest  # type: ignore
from sqlalchemy import Column  # type: ignore
from sqlalchemy import String  # type: ignore

from services.sql_database import SQLDatabase
from testing.builder import Builder


@pytest.fixture
def temporary_directory() -> str:  # type: ignore  # pylint: disable=C0116  # noqa: D103
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def sql_database(  # type: ignore  # pylint: disable=C0116  # noqa: D103
    temporary_directory: AnyStr,  # pylint: disable=W0621
) -> SQLDatabase:
    os.getcwd = Mock(return_value=temporary_directory)
    yield SQLDatabase()


class TestSQLDatabase:  # pylint: disable=C0115  # noqa: D101, W0621
    def test_setup(  # pylint: disable=C0116  # noqa: D102
        self, temporary_directory: AnyStr, sql_database: SQLDatabase  # pylint: disable=W0621
    ) -> None:
        assert os.path.exists(sql_database._db_directory)  # pylint: disable=W0212
        assert os.path.exists(f"{temporary_directory}/output/database.db")  # type: ignore
        assert f"{temporary_directory}/output" == sql_database._db_directory  # type: ignore  # pylint: disable=W0212

    def test_create_and_insert_to_table_and_truncate(  # pylint: disable=C0116, W0621  # noqa: D102
        self, sql_database: SQLDatabase
    ) -> None:
        table_name = Builder().build_random_string()
        column_names = [Column(Builder().build_random_string(), type_=String) for _ in range(5)]

        sql_database.create_table(table_name=table_name, columns=column_names)

        assert table_name in sql_database.engine.table_names()

        table_values = [[Builder().build_random_string() for _ in range(5)] for _ in range(5)]
        for values in table_values:
            sql_database.insert_into_table(
                table_name=table_name, column_names=column_names, values=[f"'{value}'" for value in values]
            )

        with sql_database.engine.connect() as connection:
            result = connection.execute(f"SELECT * FROM {table_name}").fetchall()
            assert list(map(list, result)) == table_values

        sql_database.truncate_table(table_name=table_name)

        with sql_database.engine.connect() as connection:
            result = connection.execute(f"SELECT * FROM {table_name}").fetchall()
            assert result == []
