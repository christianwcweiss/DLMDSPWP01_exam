from typing import List

import pandas as pd

from exceptions.exceptions import DatasetsDoNotMatch


class Dataset:
	def __init__(self, x: pd.Series, y: pd.Series) -> None:
		self._df = pd.DataFrame({"x": x, "y": y}).sort_values(by="x")

	@property
	def x(self) -> pd.Series:
		return self._df["x"]

	@property
	def y(self) -> pd.Series:
		return self._df["y"]

	def least_square_to_other_dataset(self, other_dataset: "Dataset") -> float:
		if not self.x.equals(other_dataset.x):
			raise DatasetsDoNotMatch(f"The coordinates of {list(self.x)} and {list(other_dataset.x)}")

		return sum((self.y - other_dataset.y) ** 2) ** 0.5