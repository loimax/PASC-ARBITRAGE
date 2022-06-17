import pandas as pd
import sqlite3

conn = sqlite3.connect('GestionRegionale.db')
cursor = conn.cursor()


def display_table(name_table):
    # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    cursor.execute(f"SELECT * FROM {name_table} WHERE index LIKE 1;")
    result = cursor.fetchall()
    
    # loop through the rows
    for row in result:
        print(row)

display_table("CLUB")