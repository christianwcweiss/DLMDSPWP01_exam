from typing import List

import pandas as pd


class Dataset:
	def __init__(self, dataset: pd.DataFrame) -> None:
		self.dataset = dataset

	def least_square_sum_to_other_dataset(self, other_dataset: "Dataset") -> float:
		return 0.0