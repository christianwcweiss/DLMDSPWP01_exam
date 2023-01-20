from typing import List, Set

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
		self.assert_datasets_match(other_dataset)

		return sum((self.y - other_dataset.y) ** 2) ** 0.5

	def get_dataset_union(self, other_dataset: "Dataset") -> Set[float]:
		return set(self.x) & set(other_dataset.x)

	def assert_datasets_match(self, other_dataset: "Dataset") -> None:
		dataset_union = self.get_dataset_union(other_dataset)
		if len(self.x) != len(dataset_union) or len(other_dataset.x) != len(dataset_union) or len(self.x) != len(other_dataset.x):
			raise DatasetsDoNotMatch(f"The datasets do not match in x!")
