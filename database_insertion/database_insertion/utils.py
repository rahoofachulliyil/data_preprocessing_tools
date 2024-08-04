import pandas as pd
import psycopg2

from .custom_exceptions import (
    EmptyHostnameInputError,
    EmptyDatabaseInputError,
    EmptyPortInputError,
    EmptyUserInputError,
    EmptyPasswordInputError,
    EmptyQueryInput,
    ColumnNameNotMatchError,
)
from string import Template


def get_operations(operations: dict, credentials: dict, DataFrame: pd.DataFrame):
    try:
        hostname = credentials["hostname"]
        database = credentials["database"]
        port = credentials["port"]
        user = credentials["user"]
        password = credentials["password"]
        action_type = [*operations.keys()][0]
        if hostname is None:
            raise EmptyHostnameInputError("Empty hostname column")
        if database is None:
            raise EmptyDatabaseInputError("Database name not given")
        if port is None:
            raise EmptyPortInputError("Port number not given")
        if user is None:
            raise EmptyUserInputError("User not given")
        if password is None:
            raise EmptyPasswordInputError("password not given")
        con = psycopg2.connect(
            host=hostname,
            database=database,
            port=int(port),
            user=user,
            password=password,
        )
        list1 = []
        if action_type == "Operation":
            column_name = operations["Operation"]["column_name"]
            table = operations["Operation"]["table"]
            operation = operations["Operation"]["operations"]
            schema = operations["Operation"]["schema"]

            # q = f"""SELECT COLUMN_NAME
            # FROM INFORMATION_SCHEMA.COLUMNS
            # WHERE TABLE_NAME = N'{table}'"""
            cur = con.cursor()
            # cur.execute(q)
            b = f'''SELECT * from {schema}."{table}"'''

            cur.execute(b)
            # a = cur.fetchall()
            con.commit()
            # print(f"hgggggg{a}")
            df_column_name = DataFrame.columns
            print(f"hjk {[df_column_name]}")
            df_column_names = []
            for i in df_column_name:
                df_column_names.append(i)
            print(f"hjk {df_column_names}")
            column_names = [desc[0] for desc in cur.description]
            print(f"hjk{column_names}")
            txt = column_name.split(",")
            # txt.sort()
            # column_names.sort()

            print(txt)
            if column_names != txt:
                raise ColumnNameNotMatchError("column name not match")
            if column_names != df_column_names:
                raise ColumnNameNotMatchError("column name not match")

            list1 = []
            if operation == "CREATE":
                query_source_template = Template(
                    'CREATE TABLE $schema."$TableName"($column_name) '
                )
                query = query_source_template.substitute(
                    {
                        "schema": schema,
                        "TableName": table,
                        "column_name": column_name,
                    }
                )
                if query is None:
                    raise EmptyQueryInput("Query not given")

                cur.execute(f"""{query}""")
                con.commit()
                table = operations["table"]
                con.close()

            if operation == "INSERT":
                for row in DataFrame.iterrows():
                    data_dict = dict(row[1])
                    values = data_dict.values()
                    value = tuple(values)
                    list1.append(value)
                    print(list1)
                txt1 = column_name.split(",")
                count = len(txt1)
                val = "%s"
                for i in range(count - 1):
                    val = val + "," + "%s"
                print(val)
                query_source_template = Template(
                    'INSERT INTO $schema."$TableName"($column_name) VALUES ($val) '
                )
                query = query_source_template.substitute(
                    {
                        "schema": schema,
                        "TableName": table,
                        "column_name": column_name,
                        "val": val,
                    }
                )
                if query is None:
                    raise EmptyQueryInput("Query not given")
                cur = con.cursor()
                for value in list1:
                    cur.execute(f"""{query}""", value)
                    con.commit()
                if table is not None:
                    df = table_not_none(cur, table, schema)
                    return df
                con.close()
            if operation == "SELECT":
                cur = con.cursor()
                df = table_not_none(cur, table, schema)
                con.close()
                return df

        if action_type == "General_Query":
            general_query = operations["General_Query"]["general_query"]
            cur = con.cursor()
            cur.execute(f"""{general_query}""")
            con.commit()
            table = operations["General_Query"]["table"]
            if table != "":
                df = table_not_none(cur, table, schema)
                return df
            con.close()
    except Exception as exec:
        raise exec


def table_not_none(cur, table, schema):
    query_string = f'''select * from {schema}."{table}"'''
    cur.execute(query_string)
    df = cur.fetchall()
    print(df)
    column_names = [desc[0] for desc in cur.description]
    if df == []:
        list = []
        for i in range(0, len(column_names)):
            list.append("null")
        tupl = tuple(list)
        df.append(tupl)

    df = pd.DataFrame(df)
    df.columns = column_names
    for item in column_names:
        df[item] = df[item].astype(str)
    print(f"print df {df}")
    return df
