"""
LOAD step of the ETL pipeline.
Writes the transformed data into a database.

By default this uses SQLite (a single file, zero setup) so beginners
and GitHub Actions can run it with no extra services.

Later, you can switch to PostgreSQL by just changing DATABASE_URL to
something like: postgresql://user:password@host:5432/etl
"""

from sqlalchemy import create_engine
import pandas as pd


def load_data(df: pd.DataFrame, database_url: str, table_name: str = "customers") -> None:
    """Write a DataFrame to the given database."""
    engine = create_engine(database_url)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False,
    )
    print(f"[LOAD] Wrote yes yes {len(df)} rows to table '{table_name}' at {database_url}")
