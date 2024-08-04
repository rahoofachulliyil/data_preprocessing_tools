import pytest
from source import process
from custom_exceptions import EmptyInputDataframeError, ColumnValidationError

import pandas as pd
from pandas._testing import assert_frame_equal


@pytest.fixture
def df():
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
            "cmpcod": ["IBS", "IBS", "IBS", "IBS", "IBS", "IBS"],
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


df_expected_for_operator_left = pd.DataFrame(
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
        "cmpcod": ["AAAIBS", "AAAIBS", "AAAIBS", "AAAIBS", "AAAIBS", "AAAIBS"],
        "x1": [
            20.9546596790604,
            18.3133402561916,
            21.569927987912,
            19.5157254553178,
            25.3596307464949,
            22.3596307464949,
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
df_expected_for_operator_right = pd.DataFrame(
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
        "cmpcod": ["IBSAAA", "IBSAAA", "IBSAAA", "IBSAAA", "IBSAAA", "IBSAAA"],
        "x1": [
            20.9546596790604,
            18.3133402561916,
            21.569927987912,
            19.5157254553178,
            25.3596307464949,
            22.3596307464949,
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
df_expected_for_operator_both = pd.DataFrame(
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
        "cmpcod": ["AIBSAA", "AIBSAA", "AIBSAA", "AIBSAA", "AIBSAA", "AIBSAA"],
        "x1": [
            20.9546596790604,
            18.3133402561916,
            21.569927987912,
            19.5157254553178,
            25.3596307464949,
            22.3596307464949,
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


def test_process_input_df_is_empty():
    df_test = None
    col = "Category"
    value = "15"
    operator = "right"
    character = "A"

    input = {
        "data": df_test,
        "config": {
            "Column_padding": {
                "columns": col,
                "string_length": value,
                "operator": operator,
                "character": character,
            }
        },
    }
    with pytest.raises(EmptyInputDataframeError):
        df_in = process(input)


def test_process_with_valid_inputs_when_operator_is_left(df):

    col = "cmpcod"
    value = "6"
    operator = "left"
    character = "A"

    input = {
        "data": df,
        "config": {
            "Column_padding": {
                "columns": col,
                "string_length": value,
                "operator": operator,
                "character": character,
            }
        },
    }

    df_in = process(input)
    print(f"Printing operator: {df_in}")
    assert_frame_equal(df_in[0], df_expected_for_operator_left)


def test_process_with_valid_inputs_when_operator_is_right(df):

    col = "cmpcod"
    value = "6"
    operator = "right"
    character = "A"

    input = {
        "data": df,
        "config": {
            "Column_padding": {
                "columns": col,
                "string_length": value,
                "operator": operator,
                "character": character,
            }
        },
    }

    df_input = process(input)

    assert_frame_equal(df_input[0], df_expected_for_operator_right)


def test_process_with_valid_inputs_when_operator_is_both(df):

    col = "cmpcod"
    value = "6"
    operator = "both"
    character = "A"

    input = {
        "data": df,
        "config": {
            "Column_padding": {
                "columns": col,
                "string_length": value,
                "operator": operator,
                "character": character,
            }
        },
    }

    df_inp = process(input)
    print(f"Printing output: {df_inp}")

    assert_frame_equal(df_inp[0], df_expected_for_operator_both)


df_expected_for_replace = pd.DataFrame(
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
        "Category": [
            "Asian_IBS",
            "Hispanic_IBS",
            "Asian_IBS",
            "European_IBS",
            "Asian_IBS",
            "European_IBS",
        ],
        "cmpcod": ["IBS", "IBS", "IBS", "IBS", "IBS", "IBS"],
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

df_expected_for_new_column = pd.DataFrame(
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
        "cmpcod": ["IBS", "IBS", "IBS", "IBS", "IBS", "IBS"],
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
        "Cat": [
            "Asian_IBS",
            "Hispanic_IBS",
            "Asian_IBS",
            "European_IBS",
            "Asian_IBS",
            "European_IBS",
        ],
    }
)


def test_process_with_valid_inputs_when_operator_is_replace(df):

    column_1 = "Category"
    column_2 = "cmpcod"
    column_name_for_replace = "Category"
    separator = "_"
    na_rep = "?"

    input = {
        "data": df,
        "config": {
            "Column_merge_with_replace": {
                "column1": column_1,
                "column2": column_2,
                "column_name_for_replace": column_name_for_replace,
                "separator": separator,
                "na_rep": na_rep,
            }
        },
    }

    df_in = process(input)
    assert_frame_equal(df_in[0], df_expected_for_replace)


def test_process_with_valid_inputs_when_operator_is_new_column(df):

    column_1 = "Category"
    column_2 = "cmpcod"

    new_column_name = "Cat"
    separator = "_"
    na_rep = "?"

    input = {
        "data": df,
        "config": {
            "Column_merge_with_new_column": {
                "column1": column_1,
                "column2": column_2,
                "new_column_name": new_column_name,
                "separator": separator,
                "na_rep": na_rep,
            }
        },
    }

    df_in = process(input)

    assert_frame_equal(df_in[0], df_expected_for_new_column)


def test_process_input_column_values_not_string_for_merge(df):

    df_test = df
    column_1 = "Category"
    column_2 = "x1"
    column_name_for_replace = "Category"
    separator = "_"
    na_rep = "?"

    input = {
        "data": df_test,
        "config": {
            "Column_merge_with_replace": {
                "column1": column_1,
                "column2": column_2,
                "column_name_for_replace": column_name_for_replace,
                "separator": separator,
                "na_rep": na_rep,
            }
        },
    }
    with pytest.raises(ColumnValidationError):
        df_in = process(input)


def test_process_input_column_values_not_string_for_padding(df):

    col = "x1"
    value = "15"
    operator = "left"
    character = "A"

    input = {
        "data": df,
        "config": {
            "Column_padding": {
                "columns": col,
                "string_length": value,
                "operator": operator,
                "character": character,
            }
        },
    }

    with pytest.raises(ColumnValidationError):
        df_in = process(input)


@pytest.fixture
def df1():
    return pd.DataFrame(
        {
            "Name": [
                "Ankit A",
                "Aishwarya A N",
                "NaN",
                "Shivangi B",
                "Ankit V Kapoor",
                "Raikit Don",
                "Sona Moorthy",
            ],
            "Age": ["30", "21", "23", "21", "24", "22", "28"],
            "Height": ["160.5", "150.2", "152.5", "158", "143.3", "143.3", "169.3"],
            "University": [
                "JNU/MGU",
                "JNU/NSU",
                "DU/GNU",
                "BHU/NGU",
                "NaN",
                "JNU/MGU",
                "DU",
            ],
        }
    )


def test_substring_1(df1):
    # expected

    input = {
        "data": df1,
        "config": {
            "substring": {
                "selected_column": "University",
                "new_column": "True",
                "new_column_name": "University_sub",
                "subsplit": "substring",
                "start_index": 0,
                "stop_index": 2,
                "step": "",
            }
        },
    }
    df1["University_sub"] = df1["University"].str.slice(0, 2)

    assert_frame_equal(process(input)[0], df1)


def test_substring_2(df1):
    # expected
    input = {
        "data": df1,
        "config": {
            "substring": {
                "selected_column": "University",
                "new_column": "True",
                "new_column_name": "University_sub",
                "subsplit": "substring",
                "start_index": 0,
                "stop_index": 1,
                "step": "",
            }
        },
    }
    df1["Age_sub"] = df1["Age"].str.slice(0, 1)

    assert_frame_equal(process(input)[0], df1)


def test_substring_3(df1):
    # expected
    input = {
        "data": df1,
        "config": {
            "substring": {
                "selected_column": "University",
                "new_column": "True",
                "new_column_name": "University_sub",
                "subsplit": "substring",
                "start_index": -3,
                "stop_index": -1,
                "step": "",
            }
        },
    }
    df1["Name_sub"] = df1["Name"].str.slice(-3, -1)

    assert_frame_equal(process(input)[0], df1)


def test_substring_4(df1):
    # expected
    print(f"Printing cong: {df1}")

    input = {
        "data": df1,
        "config": {
            "substring": {
                "selected_column": "Name",
                "new_column": "False",
                "new_column_name": "",
                "subsplit": "substring",
                "start_index": -3,
                "stop_index": -1,
                "step": "",
            }
        },
    }
    df_in = process(input)
    print(f"Printing cong: {df_in}")
    df1["Name"] = df1["Name"].str.slice(-3, -1)

    assert_frame_equal(df_in[0], df1)
