# pylint: disable=C0114  # noqa: D100
from typing import List
from typing import Tuple

from entities.point import Point


class Regressor:  # pylint: disable=R0903
    """Regressor class containing the method to find the ideal function."""

    @staticmethod
    def find_ideal_function(train_dataset: List[Point], ideal_datasets: List[List[Point]]) -> Tuple[int, float, float]:
        """Return the index, max_sum and max_deviation of the most suitable ideal function."""
        best_ideal_function = -1
        max_sum = float("inf")
        max_deviation = float("inf")
        sorted_train_dataset = sorted(train_dataset, key=lambda point: point.x_coordinate)
        for i, ideal_dataset in enumerate(ideal_datasets):
            least_squares = []
            sorted_ideal_dataset = sorted(ideal_dataset, key=lambda point: point.x_coordinate)
            for point_a, point_b in zip(sorted_train_dataset, sorted_ideal_dataset):
                least_squares.append(point_a.calculate_least_square_difference(point_b))

            least_squares_sum = sum(least_squares)
            if least_squares_sum < max_sum:
                best_ideal_function = 1 + i
                max_sum = least_squares_sum
                max_deviation = max(least_squares)

        return best_ideal_function, max_sum, max_deviation
