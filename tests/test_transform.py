import os
import sys
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from transform import transform_data


def test_email_is_lowercased():
    df = pd.DataFrame({
        "id": [1],
        "name": [" John "],
        "email": ["JOHN@EXAMPLE.COM"],
        "age": [25],
        "country": ["Canada"],
    })

    result = transform_data(df)

    assert result.loc[0, "email"] == "john@example.com"


def test_name_is_stripped():
    df = pd.DataFrame({
        "id": [1],
        "name": ["  Sarah  "],
        "email": ["sarah@example.com"],
        "age": [32],
        "country": ["Canada"],
    })

    result = transform_data(df)

    assert result.loc[0, "name"] == "Sarah"


def test_age_group_young_vs_adult():
    df = pd.DataFrame({
        "id": [1, 2],
        "name": ["A", "B"],
        "email": ["a@example.com", "b@example.com"],
        "age": [25, 41],
        "country": ["Canada", "USA"],
    })

    result = transform_data(df)

    assert result.loc[0, "age_group"] == "Young"
    assert result.loc[1, "age_group"] == "Adult"


def test_duplicates_are_dropped():
    df = pd.DataFrame({
        "id": [1, 1],
        "name": ["John", "John"],
        "email": ["john@example.com", "john@example.com"],
        "age": [25, 25],
        "country": ["Canada", "Canada"],
    })

    result = transform_data(df)

    assert len(result) == 1
