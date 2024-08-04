import pytest
from source import process
from custom_exceptions import (
    
    EmptyHostnameInputError,
    EmptyDatabaseInputError,
    EmptyUserInputError,
    EmptyPortInputError,

    EmptyPasswordInputError,
)



def test_empty_hostname_input():

    hostname = None
    database = "Test_DB"
    user = "postgres"
    port = 5432
    password = "manager123"
    # operations = "INSERT"
    # column_name = "event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail"
    table = "Transaction_Log"

    input = {
     
        "config": {
            "hostname": hostname,
            "database": database,
            "user": user,
            "port": port,
            "password": password,
             "table": "Transaction_Log",
             "schema":"public"
        },
       
    }
    with pytest.raises(EmptyHostnameInputError):
        df_in = process(input)


def test_empty_database_input():
  
    hostname = "localhost"
    database = None
    user = "postgres"
    port = 5432
    password = "manager123"
    # operations = "INSERT"
    # column_name = "event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail"
    table = "Transaction_Log"

    input = {
       
        "config": {
            "hostname": hostname,
            "database": database,
            "user": user,
            "port": port,
            "password": password,
            "table": "Transaction_Log",
             "schema":"public"
        },
         
    }
    with pytest.raises(EmptyDatabaseInputError):
        df_in = process(input)


def test_empty_user_input():
    
    hostname = "localhost"
    database = "Test_DB"
    user = None
    port = 5432
    password = "manager123"
    # operations = "INSERT"
    # column_name = "event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail"
    table = "Transaction_Log"

    input = {
       
        "config": {
            "hostname": hostname,
            "database": database,
            "user": user,
            "port": port,
            "password": password,
            "table": "Transaction_Log",
             "schema":"public"
        },
      
    }
    with pytest.raises(EmptyUserInputError):
        df_in = process(input)


def test_empty_port_input():
  
    hostname = "localhost"
    database = "Test_DB"
    user = "postgres"
    port = None
    password = "manager123"
    # operations = "INSERT"
    # column_name = "event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail"
    table = "Transaction_Log"

    input = {
        
        "config": {
            "hostname": hostname,
            "database": database,
            "user": user,
            "port": port,
            "password": password,
            "table": "Transaction_Log", "schema":"public"
        },
       
    }
    with pytest.raises(EmptyPortInputError):
        df_in = process(input)


def test_empty_password_input():
    hostname = "localhost"
    database = "Test_DB"
    user = "postgres"
    port = 5432
    password = None
    # operations = "INSERT"
    # column_name = "event_id, event_name, event_date, membership_number, activity_type, activity_date, activity_number, event_detail"
    table = "Transaction_Log"

    input = {
    
        "config": {
            "hostname": hostname,
            "database": database,
            "user": user,
            "port": port,
            "password": password,
            "table": "Transaction_Log",
             "schema":"public"
        },
       
    }
    with pytest.raises(EmptyPasswordInputError):
        df_in = process(input)
