import psycopg2
from custom_exceptions import (
    EmptyHostnameInputError,
    EmptyDatabaseInputError,
    EmptyPortInputError,
    EmptyUserInputError,
    EmptyPasswordInputError,
 
   
)



def process(input: dict):
    hostname = input["config"]["hostname"]
    database = input["config"]["database"]
    port = input["config"]["port"]
    user = input["config"]["user"]
    password = input["config"]["password"]
    table=input["config"]["table"]
    schema=input["config"]["schema"]
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
    query_string = f'''DELETE from {schema}."{table}"'''
    cur.execute(query_string)
    con.commit()
    con.close()
  
   