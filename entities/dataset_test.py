import math

import pytest

from entities.dataset import Dataset
from exceptions.exceptions import DatasetsDoNotMatch
from testing.builder import Builder


class TestDataset:
	def test_dataset_creation(self) -> None:
		x = Builder.build_random_data_series(0, 100, rows=100).sort_values(ignore_index=True)
		y = Builder.build_random_data_series(0, 100, rows=100)

		dataset = Dataset(x, y)

		assert dataset.x.equals(x)
		assert dataset.y.equals(y)

	def test_least_square_sum_to_other_dataset(self) -> None:
		x = Builder.build_random_data_series(0, 100, rows=100)
		y = Builder.build_random_data_series(0, 100, rows=100)
		other_y = Builder.build_random_data_series(0, 100, rows=100)
		dataset = Dataset(x, y)
		other_dataset = Dataset(x, other_y)

		least_square = dataset.least_square_to_other_dataset(other_dataset)

		assert math.isclose(least_square, sum([abs(y1 - y2) ** 2 for y1, y2 in zip(y, other_y)]) ** 0.5)
		assert math.isclose(dataset.least_square_to_other_dataset(dataset), 0.0)

	def test_datasets_do_not_match_length(self) -> None:
		x = Builder.build_random_data_series()
		y = Builder.build_random_data_series()
		dataset = Dataset(x, y)
		other_dataset = Dataset(x[:-5], y[:-5])

		with pytest.raises(DatasetsDoNotMatch):
			dataset.least_square_to_other_dataset(other_dataset)

	def test_datasets_do_not_match_in_x(self) -> None:
		x1 = Builder.build_random_data_series()
		x2 = Builder.build_random_data_series()
		y = Builder.build_random_data_series()
		dataset = Dataset(x1, y)
		other_dataset = Dataset(x2, y)

		with pytest.raises(DatasetsDoNotMatch):
			dataset.least_square_to_other_dataset(other_dataset)