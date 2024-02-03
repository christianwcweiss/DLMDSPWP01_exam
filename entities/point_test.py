# pylint: disable=C0114  # noqa: D100
import pytest  # type: ignore

from entities.point import Point
from exceptions.exceptions import PointsDoNotMatchInX
from testing.builder import Builder


class TestPoint:  # pylint: disable=C0115  # noqa: D101
    def test_points_do_not_match_in_x(self) -> None:  # pylint: disable=C0116  # noqa: D102
        x_coordinate = Builder().build_random_float_number()
        other_x_coordinate = Builder().build_random_float_number(x_coordinate + 1.0)
        point = Builder.build_random_point(x_coordinate=x_coordinate)
        other_point = Builder.build_random_point(x_coordinate=other_x_coordinate)

        with pytest.raises(PointsDoNotMatchInX):
            point.calculate_least_square_difference(other_point)

    @pytest.mark.parametrize(
        "point, other_point, expected_result",
        [[Point(1.0, 1.0), Point(1.0, 1.0), 0.00], [Point(1.5, 1.0), Point(1.5, 3.0), 4.00]],
    )
    def test_calculate_least_square_difference(  # pylint: disable=C0116  # noqa: D102
        self, point: Point, other_point: Point, expected_result
    ) -> None:
        actual_result = point.calculate_least_square_difference(other_point=other_point)

        assert actual_result == expected_result
