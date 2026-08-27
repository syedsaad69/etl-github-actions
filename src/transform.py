"""
TRANSFORM step of the ETL pipeline.
Cleans and enriches the raw data.
"""

import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and enrich the raw data."""
    df = df.drop_duplicates()

    df["name"] = df["name"].str.strip()
    df["email"] = df["email"].str.lower()

    df["age_group"] = df["age"].apply(
        lambda age: "Young" if age < 30 else "Adult"
    )

    print(f"[TRANSFORM] Cleaned {len(df)} rows")
    return df
