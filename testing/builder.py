from typing import Union

import numpy as np
import pandas as pd


class Builder:
    """Builder class to randomize test data."""

    @classmethod
    def build_random_float_number(cls, min_value: float, max_value: float) -> Union[np.ndarray, float]:
        """Build a random float number between min_value and max_value."""
        return np.random.randn(min_value, max_value)

    @classmethod
    def build_random_data_frame(cls, min_value: int, max_value: int, rows: int = 100, columns: int = 2) -> pd.DataFrame:
        """Build a random dataframe with values between min_value and max_value and n rows and m columns."""
        return pd.DataFrame(
            np.random.randint(min_value, max_value, size=(rows, columns)),
            columns=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:columns]),
        )
