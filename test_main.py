import os
import pandas as pd


def test_input_file_exists():

    input_file = "data/employees.csv"

    assert os.path.exists(input_file)


def test_input_data():

    input_file = "data/employees.csv"

    df = pd.read_csv(input_file)

    assert len(df) == 4
    assert "employee" in df.columns
    assert "salary" in df.columns


def test_salary_calculation():

    input_file = "data/employees.csv"

    df = pd.read_csv(input_file)

    df["annual_salary"] = df["salary"] * 12

    assert df.loc[0, "annual_salary"] == 720000
    assert df.loc[2, "annual_salary"] == 900000


def test_bonus_calculation():

    input_file = "data/employees.csv"

    df = pd.read_csv(input_file)

    df["bonus"] = df["salary"].apply(
        lambda salary: salary * 0.10 if salary >= 70000 else 0
    )

    assert df.loc[0, "bonus"] == 0
    assert df.loc[2, "bonus"] == 7500