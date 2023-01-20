import os
from contextlib import contextmanager
from typing import List

from sqlalchemy import Column, String
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import create_engine


class SQLDatabase:

	def __init__(self) -> None:
		self._endpoint = os.environ.get("POSTGRES_ENDPOINT")
		self._port = os.environ.get("POSTGRES_PORT", "5432")

		self._user_name = os.environ.get("POSTGRES_USER")
		self._password = os.environ.get("POSTGRES_PASSWORD")

		connection_string = f"postgresql+psycopg2://{self._user_name}:{self._password}@{self._endpoint}:{self._port}/dlmdspwp01"
		print(f"Setting up sql alchemy engine with the connection string: {connection_string}")
		self._engine = create_engine(
			connection_string,
			pool_pre_ping=True,
			echo=True
		)


	def create_table(self, table_name: str, columns: List[Column]) -> None:
		meta = MetaData()
		table = Table(
			table_name,
			meta,
			*columns
		)

		try:
			meta.create_all(self._engine)
		except Exception as error:
			print(f"Cannot create table due to the following error: {error}")



def main():
	db = SQLDatabase()

	db.create_table("Test", [Column("test", String, primary_key=True)])


if __name__ == "__main__":
	main()