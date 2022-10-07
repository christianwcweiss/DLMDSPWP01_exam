import pandas as pd

class FileLoaderService:

	@classmethod
	def load_data(cls, directory: str) -> pd.DataFrame:
		return pd.read_csv(directory)

