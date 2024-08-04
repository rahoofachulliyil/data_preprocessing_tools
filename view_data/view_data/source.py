import pandas as pd
from typing import Dict
import psycopg2
import json
from .custom_exceptions import (
    EmptyHostnameInputError,
    EmptyDatabaseInputError,
    EmptyPortInputError,
    EmptyUserInputError,
    EmptyPasswordInputError,
 
   
)



def process(input: Dict):
    hostname = input["config"]["hostname"]
    database = input["config"]["database"]
    port = input["config"]["port"]
    user = input["config"]["user"]
    password = input["config"]["password"]
    table=input["config"]["table"]
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
    cur = con.cursor()
    query_string = f'''select * from public."{table}"'''
    cur.execute(query_string)
    data=cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    print(column_names)
    df = pd.DataFrame(data)
    df.columns = column_names
    a=df.dtypes
    print(a)
    
    for item in a.items():
        print(type(item[1]))
        k=item[1]
        c=item[0]
        print(c)
        # l=df[c]
        # print(f"hhhhhhh{(l)}")
        # dictionary = l.to_json()
        # print(dictionary)
        # if k == 'datetime64[ns, UTC]':
        df[c]= df[c].astype(str)
        # if tydf[c] is dict:
        #          dictionary[key] = json.dumps(dictionary[key])
    b=df.dtypes
    print(f"print data type {b}")
    print(df)
    return [df]
  
   