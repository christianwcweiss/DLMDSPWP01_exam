from typing import Union

import pandas as pd
import numpy as np


class Builder:
	@classmethod
	def build_random_float_number(cls, min_value: float, max_value: float) -> Union[np.ndarray, float]:
		return np.random.randn(min_value, max_value)

	@classmethod
	def build_random_data_frame(cls, min_value: int, max_value: int, rows: int = 100, columns: int = 2) -> pd.DataFrame:
		return pd.DataFrame(np.random.randint(min_value, max_value, size=(rows, columns)), columns=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:columns]))
