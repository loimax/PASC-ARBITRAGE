import pandas as pd
import sqlite3
import os

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    if os.path.exists(db_file):
        conn = sqlite3.connect(db_file)
        return conn
    else:
        print("Error: Database not found")
        exit(1)
      
def show_tables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    result = cursor.fetchall()
    i = 1
    for row in result:
        print(f"{i} : {row[0]}")
        i += 1

def display_attributes(name_table):
    cols = pd.read_sql_query(f"SELECT * from {name_table}", conn)
    strtables = []
    for cols in cols.columns:
        strtables.append(cols)
    print(strtables) #affiche liste complète attributs

def display_table(name_table, specified=False, num_rows=0):
    
    cursor.execute(f"SELECT * FROM {name_table};")
    cols = pd.read_sql_query(f"SELECT * from {name_table}", conn)
    if specified:
        result = cursor.fetchmany(num_rows)
    else:
        result = cursor.fetchall()
        
    strtables = " | ".join(cols.columns)
    print("\n", strtables, "\n")
    for row in result:
        print(row) #print(row[1]) affiche 1re colonne de la table

def insert_value(name_table):
    cursor.execute(f"INSERT INTO {name_table} VALUES (18, 'TestOpen', '2022/020203', '1200', '04180613', 3, 1)")
    conn.commit()


conn = create_connection("testdb\GestionRegionale.db")
cursor = conn.cursor()

#show_tables()
#display_attributes("CLUB")
# insert_value("Epreuves")
display_table("CLUB")