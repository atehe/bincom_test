"""Python script that connects to a mysql server and creates the database (from bincom_test.sql file)"""

import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name, user=user_name, passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name, user=user_name, passwd=user_password, database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        columns_name = [description[0].upper() for description in cursor.description]
        result.insert(0, columns_name)  # Appends column header to the fetchall data
        return result
    except Error as err:
        print(f"Error: {err}'")


def main():

    PASSWORD = "root"

    server_connection = create_server_connection("localhost", "root", PASSWORD)
    create_database(server_connection, "CREATE DATABASE bincom_test")
    db_connection = create_db_connection("localhost", "root", PASSWORD, "bincom_test")

    with open("database_template/bincom_test.sql") as sql_file:
        sql_as_string = sql_file.read()

    execute_query(db_connection, sql_as_string)


if __name__ == "__main__":
    main()
