"""
Runs the full ETL pipeline: Extract -> Transform -> Load.

Run it with:
    python src/main.py
"""

import os
import sys

# Allow running this file directly (python src/main.py)
sys.path.append(os.path.dirname(__file__))

from extract import extract_data
from transform import transform_data
from load import load_data


def main():
    # Project root = one folder up from this file (src/), so this works
    # no matter what directory you run the script from.
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(project_root, "data", "customers.csv")

    # 1. EXTRACT
    data = extract_data(csv_path)

    # 2. TRANSFORM
    transformed_data = transform_data(data)

    # 3. LOAD
    # DATABASE_URL can be overridden via an environment variable.
    # Default: a local SQLite file called etl.db (no setup required).
    database_url = os.environ.get("DATABASE_URL", "sqlite:///etl.db")
    load_data(transformed_data, database_url)

    print("\n✅ ETL pipeline completed successfully!")


if __name__ == "__main__":
    main()
