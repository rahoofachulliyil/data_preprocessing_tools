import pytest
import pandas as pd
from source import process
from custom_exceptions import (
    InputNotFoundException,
    ColumnNameNotMatchError,
    CannotMapInputsException,
)
from pandas._testing import assert_frame_equal


@pytest.fixture
def df():
    return pd.DataFrame(
        {
            "tircod": [
                '{"cmpcod":"IBS","tircod":"403","memtle":"U","memgnd":"U","cty":"kochi","prgcod":"PRG","memshptyp":"I","enrsrc":"C","age":"20","country":"India","currency":"INR"}',
                '{"cmpcod":"IBS","tircod":"402","memtle":"DR","memgnd":"M","cty":"thrissur","prgcod":"PRG","memshptyp":"I","enrsrc":"W","age":"21","country":"India","currency":"INR"}',
                '{"cmpcod":"IBS","tircod":"405","memtle":"U","memgnd":"U","cty":"malappuram","prgcod":"PRG","memshptyp":"I","enrsrc":"C","age":"22","country":"India","currency":"INR"}',
                '{"cmpcod":"IBS","tircod":"500","memtle":"MR","memgnd":"F","cty":"dubai","prgcod":"PRG","memshptyp":"I","enrsrc":"C","age":"25","country":"UAE","currency":"dirham"}',
                '{"cmpcod":"IBS","tircod":"501","memtle":"MR","memgnd":"F","cty":"dubai","prgcod":"PRG","memshptyp":"I","enrsrc":"C","age":"25","country":"UAE","currency":"dirham"}',
            ]
        }
    )


@pytest.fixture
def path():
    return pd.DataFrame(
        {
            "Column_names": [
                "cmpcod",
                "tircod",
                "memtle",
                "memgnd",
                "cty",
                "prgcod",
                "memshptyp",
                "enrsrc",
                "age",
                "country",
                "currency",
            ]
        }
    )


@pytest.fixture
def paths():
    return pd.DataFrame(
        {
            "Column_names": [
                "cmpco",
                "tircod",
                "memtle",
                "memgnd",
                "cty",
                "prgcod",
                "memshptyp",
                "enrsrc",
                "age",
                "country",
                "currency",
            ]
        }
    )


@pytest.fixture
def path1():
    return pd.DataFrame(
        {
            "Column_names": [
                "cmpcod",
                "tircod",
                "memtle",
                "memgnd",
                "cty",
                "prgcod",
                "memshptyp",
                "enrsrc",
                "age",
                "country",
            ]
        }
    )


@pytest.fixture
def path2():
    return pd.DataFrame(
        {
            "Column_names": [
                "cmpcod",
                "tircod",
                "memtle",
                "memgnd",
                "cty",
                "prgcod",
                "memshptyp",
                "enrsrc",
                "age",
                "country",
                "currency",
                "Area",
            ]
        }
    )


df_expected = pd.DataFrame(
    {
        "cmpcod": ["IBS", "IBS", "IBS", "IBS", "IBS"],
        "tircod": ["403", "402", "405", "500", "501"],
        "memtle": ["U", "DR", "U", "MR", "MR"],
        "memgnd": ["U", "M", "U", "F", "F"],
        "cty": ["kochi", "thrissur", "malappuram", "dubai", "dubai"],
        "prgcod": ["PRG", "PRG", "PRG", "PRG", "PRG"],
        "memshptyp": ["I", "I", "I", "I", "I"],
        "enrsrc": ["C", "W", "C", "C", "C"],
        "age": ["20", "21", "22", "25", "25"],
        "country": ["India", "India", "India", "UAE", "UAE"],
        "currency": ["INR", "INR", "INR", "dirham", "dirham"],
    }
)


@pytest.fixture
def df1():
    return pd.DataFrame(
        {
            "tircod": [
                '{"cmpco":"IBS","tircod":"403","memtle":"U","memgnd":"U","cty":"kochi","prgcod":"PRG","memshptyp":"I","enrsrc":"C","age":"20","country":"India","currency":"INR"}',
                '{"cmpco":"IBS","tircod":"402","memtle":"DR","memgnd":"M","cty":"thrissur","prgcod":"PRG","memshptyp":"I","enrsrc":"W","age":"21","country":"India","currency":"INR"}',
                '{"cmpco":"IBS","tircod":"405","memtle":"U","memgnd":"U","cty":"malappuram","prgcod":"PRG","memshptyp":"I","enrsrc":"C","age":"22","country":"India","currency":"INR"}',
                '{"cmpco":"IBS","tircod":"500","memtle":"MR","memgnd":"F","cty":"dubai","prgcod":"PRG","memshptyp":"I","enrsrc":"C","age":"25","country":"UAE","currency":"dirham"}',
                '{"cmpco":"IBS","tircod":"501","memtle":"MR","memgnd":"F","cty":"dubai","prgcod":"PRG","memshptyp":"I","enrsrc":"C","age":"25","country":"UAE","currency":"dirham"}',
            ]
        }
    )


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


def test_process_to_check_equal(df, path):

    input = {"data": df, "column_data": path}
    df_in = process(input)
    assert_frame_equal(df_in[0], df_expected)


def test_process_input_column_not_match(df, paths):
    df = df
    input = {"data": df, "column_data": paths}
    with pytest.raises(ColumnNameNotMatchError):
        df_in = process(input)


def test_process_input_column_less(df, path1):
    df = df
    input = {"data": df, "column_data": path1}
    with pytest.raises(CannotMapInputsException):
        df_in = process(input)


def test_process_input_column_more(df, path2):
    df = df
    input = {"data": df, "column_data": path2}
    with pytest.raises(CannotMapInputsException):
        df_in = process(input)


def test_process_input_column_not_match1(df1, path):
    df = df1
    input = {"data": df, "column_data": path}
    with pytest.raises(ColumnNameNotMatchError):
        df_in = process(input)
