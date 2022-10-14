import random
from typing import Union

import numpy as np
import pandas as pd


class Builder:
    """Builder class to randomize test data."""

    @classmethod
    def build_random_float_number(cls, min_value: float = 0.0, max_value: float = 100.0) -> float:
        """Build a random float number between min_value and max_value."""
        return random.uniform(min_value, max_value)


    @classmethod
    def build_random_data_series(cls, min_value: float = 0.0, max_value: float = 100.0, rows: int = 100) -> pd.Series:
        """Build a random dataframe with values between min_value and max_value and n rows and m columns."""
        return pd.Series(
            [cls.build_random_float_number(min_value, max_value) for _ in range(rows)],
            index=[index for index in range(rows)]
        )
