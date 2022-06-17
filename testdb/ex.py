from xmlrpc.client import boolean
import pandas as pd
import sqlite3

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    return conn

def show_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    result = cursor.fetchall()
    i = 1
    for row in result:
        print(f"{i} : {row[0]}")
        i += 1

def display_table(name_table, specified=False, num_rows=0):
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    cursor.execute(f"SELECT * FROM {name_table};")
    if specified:
        result = cursor.fetchmany(num_rows)
        # loop through the rows
        for row in result:
            print(row)
    else:
        result = cursor.fetchall()
        # loop through the rows
        for row in result:
            print(row)

conn = create_connection("GestionRegionale.db")
cursor = conn.cursor()

display_table("CLUB", True, 5)