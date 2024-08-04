import pytest
from source import process
from custom_exceptions import (
    EmptyInputDataframeError,
    EmptyHostnameInputError,
    EmptyDatabaseInputError,
    EmptyUserInputError,
    EmptyPortInputError,
    ColumnNameNotMatchError,
    EmptyPasswordInputError,
)
import pandas as pd


# from pandas._testing import assert_frame_equal
df = pd.read_csv("Transaction.csv")


def test_process_input_df_is_empty():
    df_test = None
    hostname = "localhost"
    database = "Test_DB"
    user = "postgres"
    port = 5432
    password = "manager123"
    operations = "INSERT"
    column_name = "event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail"
    table = "Transaction_Log"

    input = {
        "data": df_test,
        "config": {
            "hostname": hostname,
            "database": database,
            "user": user,
            "port": port,
            "password": password,
        },
        "operation_config": {
            "Operation": {
                "operations": operations,
                "column_name": column_name,
                "table": table,
            },
        },
    }
    with pytest.raises(EmptyInputDataframeError):
        df_in = process(input)


def test_empty_hostname_input():
    df_test = df
    hostname = None
    database = "Test_DB"
    user = "postgres"
    port = 5432
    password = "manager123"
    operations = "INSERT"
    column_name = "event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail"
    table = "Transaction_Log"

    input = {
        "data": df_test,
        "config": {
            "hostname": hostname,
            "database": database,
            "user": user,
            "port": port,
            "password": password,
        },
        "operation_config": {
            "Operation": {
                "operations": operations,
                "column_name": column_name,
                "table": table,
            },
        },
    }
    with pytest.raises(EmptyHostnameInputError):
        df_in = process(input)


def test_empty_database_input():
    df_test = df
    hostname = "localhost"
    database = None
    user = "postgres"
    port = 5432
    password = "manager123"
    operations = "INSERT"
    column_name = "event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail"
    table = "Transaction_Log"

    input = {
        "data": df_test,
        "config": {
            "hostname": hostname,
            "database": database,
            "user": user,
            "port": port,
            "password": password,
        },
        "operation_config": {
            "Operation": {
                "operations": operations,
                "column_name": column_name,
                "table": table,
            },
        },
    }
    with pytest.raises(EmptyDatabaseInputError):
        df_in = process(input)


def test_empty_user_input():
    df_test = df
    hostname = "localhost"
    database = "Test_DB"
    user = None
    port = 5432
    password = "manager123"
    operations = "INSERT"
    column_name = "event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail"
    table = "Transaction_Log"

    input = {
        "data": df_test,
        "config": {
            "hostname": hostname,
            "database": database,
            "user": user,
            "port": port,
            "password": password,
        },
        "operation_config": {
            "Operation": {
                "operations": operations,
                "column_name": column_name,
                "table": table,
            },
        },
    }
    with pytest.raises(EmptyUserInputError):
        df_in = process(input)


def test_empty_port_input():
    df_test = df
    hostname = "localhost"
    database = "Test_DB"
    user = "postgres"
    port = None
    password = "manager123"
    operations = "INSERT"
    column_name = "event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail"
    table = "Transaction_Log"

    input = {
        "data": df_test,
        "config": {
            "hostname": hostname,
            "database": database,
            "user": user,
            "port": port,
            "password": password,
        },
        "operation_config": {
            "Operation": {
                "operations": operations,
                "column_name": column_name,
                "table": table,
            },
        },
    }
    with pytest.raises(EmptyPortInputError):
        df_in = process(input)


def test_empty_password_input():
    df_test = df
    hostname = "localhost"
    database = "Test_DB"
    user = "postgres"
    port = 5432
    password = None
    operations = "INSERT"
    column_name = "event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail"
    table = "Transaction_Log"

    input = {
        "data": df_test,
        "config": {
            "hostname": hostname,
            "database": database,
            "user": user,
            "port": port,
            "password": password,
        },
        "operation_config": {
            "Operation": {
                "operations": operations,
                "column_name": column_name,
                "table": table,
            },
        },
    }
    with pytest.raises(EmptyPasswordInputError):
        df_in = process(input)


def test_column_not_match():
    df_test = df
    hostname = "localhost"
    database = "Test_DB"
    user = "postgres"
    port = 5432
    password = "manager123"
    operations = "INSERT"
    column_name = "event_name,event_date,membership_number,activity_type,activity_date,activity_number,event_detail"
    table = "Transaction_Log"

    input = {
        "data": df_test,
        "config": {
            "hostname": hostname,
            "database": database,
            "user": user,
            "port": port,
            "password": password,
        },
        "operation_config": {
            "Operation": {
                "operations": operations,
                "column_name": column_name,
                "table": table,
                "schema": "public",
            },
        },
    }
    with pytest.raises(ColumnNameNotMatchError):
        df_in = process(input)
