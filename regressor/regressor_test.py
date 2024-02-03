# pylint: disable=C0114  # noqa: D100
import pytest  # type: ignore

from entities.point import Point
from regressor.regressor import Regressor


class TestRegressor:  # pylint: disable=C0115  # noqa: D101
    def test_find_ideal_function_with_empty_datasets(self):  # pylint: disable=C0116  # noqa: D102
        train_dataset = []
        ideal_datasets = [[]]

        with pytest.raises(ValueError):
            _, _, _ = Regressor.find_ideal_function(train_dataset, ideal_datasets)

    def test_find_ideal_function_with_identical_datasets(self):  # pylint: disable=C0116  # noqa: D102
        train_dataset = [Point(1, 2), Point(3, 4), Point(5, 6)]
        ideal_datasets = [[Point(1, 2), Point(3, 4), Point(5, 6)]]

        best_ideal_function, max_sum, max_deviation = Regressor.find_ideal_function(train_dataset, ideal_datasets)

        assert best_ideal_function == 1
        assert max_sum == 0.0
        assert max_deviation == 0.0

    def test_find_ideal_function_with_different_datasets(self):  # pylint: disable=C0116  # noqa: D102
        train_dataset = [Point(1, 2), Point(3, 4), Point(5, 6)]
        ideal_datasets = [[Point(2, 3), Point(4, 5), Point(6, 7)]]

        best_ideal_function, max_sum, max_deviation = Regressor.find_ideal_function(train_dataset, ideal_datasets)

        assert best_ideal_function == -1
        assert max_sum == float("inf")
        assert max_deviation == float("inf")

    def test_find_ideal_function_with_multiple_ideal_datasets(self):  # pylint: disable=C0116  # noqa: D102
        train_dataset = [Point(1, 2), Point(3, 4), Point(5, 6)]
        ideal_datasets = [
            [Point(1, 3), Point(3, 5), Point(5, 7)],
            [Point(3, 4), Point(1, 2), Point(5, 6)],
            [Point(1, 1), Point(3, 3), Point(5, 5)],
        ]

        best_ideal_function, max_sum, max_deviation = Regressor.find_ideal_function(train_dataset, ideal_datasets)

        assert best_ideal_function == 2
        assert max_sum == 0.0
        assert max_deviation == 0.0
