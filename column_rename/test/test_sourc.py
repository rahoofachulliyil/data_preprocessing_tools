import pytest
import pandas as pd
from custom_exceptions import EmptyInputDataframeError
from source import process
from pandas._testing import assert_frame_equal
@pytest.fixture

def df():
    return pd.read_csv("memdet_final.csv")
@pytest.fixture
def columns():
     return pd.read_csv("column_rename.csv")
@pytest.fixture
def df1():
 return pd.DataFrame(
    {
        "BOOKING_DATE": [
            "2015-07-31 22:00:00",
            "2016-12-05 8:00:00",
            "2014-08-10 12:00:00",
            "2019-11-18 7:00:00",
            "2014-07-19 20:00:00",
            "2020-12-31 7:00:00",
        ],
        "FLIGHT_DATE": [
            "2019-11-23 7:00:00",
            "2019-12-18 18:00:00",
            "2018-08-11 13:00:00",
            "2019-11-30 19:00:00",
            "2019-07-21 15:00:00",
            "2021-01-07 18:00:00",
        ],
        "Category": ["Asian", "Hispanic", "Asian", "European", "Asian", "European"],
         "cmpcod":["IBS","IBS","IBS","IBS","IBS","IBS"],
         
        "x1": [
            20.954659679060413,
            18.31334025619164,
            21.569927987912035,
            19.515725455317845,
            25.359630746494982,
            22.359630746494982,
        ],
        "x2": [
            28.403124298916406,
            26.808441325755354,
            29.993373813579744,
            30.369820500803115,
            25.60606661210394,
            32.369820500803115,
        ],
    }
)
@pytest.fixture
def columns1():
 return pd.DataFrame({
     "current_column_name":["x1","x2"],
     "new_column_name":["xx1","xx2"]

 })
df_expected=pd.DataFrame(
    {
        "BOOKING_DATE": [
            "2015-07-31 22:00:00",
            "2016-12-05 8:00:00",
            "2014-08-10 12:00:00",
            "2019-11-18 7:00:00",
            "2014-07-19 20:00:00",
            "2020-12-31 7:00:00",
        ],
        "FLIGHT_DATE": [
            "2019-11-23 7:00:00",
            "2019-12-18 18:00:00",
            "2018-08-11 13:00:00",
            "2019-11-30 19:00:00",
            "2019-07-21 15:00:00",
            "2021-01-07 18:00:00",
        ],
        "Category": ["Asian", "Hispanic", "Asian", "European", "Asian", "European"],
         "cmpcod":["IBS","IBS","IBS","IBS","IBS","IBS"],
         
        "xx1": [
            20.954659679060413,
            18.31334025619164,
            21.569927987912035,
            19.515725455317845,
            25.359630746494982,
            22.359630746494982,
        ],
        "xx2": [
            28.403124298916406,
            26.808441325755354,
            29.993373813579744,
            30.369820500803115,
            25.60606661210394,
            32.369820500803115,
        ],
    }
)
def test_process_input_df_is_empty(columns):
    df = None
    input = {"data": df, "column_map_info": columns}
    with pytest.raises(EmptyInputDataframeError):
        df_in = process(input)

def test_process_input_columns_is_empty(df):
    columns = None
    input = {"data": df, "column_map_info": columns}
    with pytest.raises(EmptyInputDataframeError):
        df_in = process(input)

def test_process_to_validate(df1,columns1):
        input = {"data": df1, "column_map_info": columns1}
        df_inp = process(input)
        assert_frame_equal(df_inp[0], df_expected)