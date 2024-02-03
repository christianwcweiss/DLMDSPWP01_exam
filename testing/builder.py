# pylint: disable=C0114  # noqa: D100
import random
import string
from typing import Optional

import pandas as pd  # type: ignore

from entities.point import Point


class Builder:
    """Builder class to randomize test data."""

    @classmethod
    def build_random_string(cls, length: int = 10) -> str:
        """Build a random string of length."""
        return "".join(random.choices(string.ascii_letters, k=length))

    @classmethod
    def build_random_float_number(cls, min_value: float = 0.0, max_value: float = 100.0) -> float:
        """Build a random float number between min_value and max_value."""
        return random.uniform(min_value, max_value)

    @classmethod
    def build_random_data_series(cls, min_value: float = 0.0, max_value: float = 100.0, rows: int = 100) -> pd.Series:
        """Build a random dataframe with values between min_value and max_value and n rows and m columns."""
        return pd.Series(
            [cls.build_random_float_number(min_value, max_value) for _ in range(rows)],
            index=list(range(rows)),
        )

    @classmethod
    def build_random_point(cls, x_coordinate: Optional[float] = None, y_coordinate: Optional[float] = None) -> Point:
        """Build a random point with either fixed or random values."""
        return Point(
            x_coordinate=x_coordinate or cls.build_random_float_number(),
            y_coordinate=y_coordinate or cls.build_random_float_number(),
        )
