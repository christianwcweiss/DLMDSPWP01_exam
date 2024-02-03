# pylint: disable=C0114  # noqa: D100
from exceptions.exceptions import PointsDoNotMatchInX


class Point:
    """Class representing a point with x and y."""

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        """Initialize the Point class."""
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate

    @property
    def x_coordinate(self) -> float:
        """Return the internal variable _x_coordinate."""
        return self._x_coordinate

    @property
    def y_coordinate(self) -> float:
        """Return the internal variable _y_coordinate."""
        return self._y_coordinate

    def __str__(self) -> str:
        """Override __str__ method to print the points in a better way."""
        return f"Point ({self.x_coordinate} | {self.y_coordinate})"

    def calculate_least_square_difference(self, other_point: "Point") -> float:
        """
        Calculate the least square difference between one point and another point.

        If two points don't match in x an PointsDoNotMatchInX error is thrown.
        """
        if self.x_coordinate != other_point.x_coordinate:
            raise PointsDoNotMatchInX(f"{str(self)} and {str(other_point)} do not match in x")

        return (abs(self.y_coordinate - other_point.y_coordinate)) ** 2
