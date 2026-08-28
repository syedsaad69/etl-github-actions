"""
EXTRACT step of the ETL pipeline.
Reads raw data from a CSV file into a pandas DataFrame.
"""

import pandas as pd


def extract_data(file_path: str) -> pd.DataFrame:
    """Read a CSV file and return it as a DataFrame."""
    df = pd.read_csv(file_path)
    print(f"[EXTRACT] Loaded yes yes {len(df)} rows from {file_path}")
    return df
