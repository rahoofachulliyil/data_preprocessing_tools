import pytest
import pandas as pd
from source import process
from custom_exceptions import (
    InputNotFoundException,

)
@pytest.fixture


def df():

  return (pd.read_csv("transaction_detail1.csv"))
@pytest.fixture
def path():
    return(pd.read_csv("transaction_columns2.csv"))
def test_process_input_df_is_empty(path):
    df = None
    input = {"data": df, "column_data": path}
    with pytest.raises(InputNotFoundException):
        df_in = process(input)


def test_process_input_path_is_empty(df):
    path = None
    input = {"data": df, "column_data": path}
    with pytest.raises(InputNotFoundException):
        df_in = process(input)