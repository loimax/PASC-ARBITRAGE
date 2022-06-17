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

def execute_query(query, del_ins=False):
    cursor.execute(query)
    if del_ins:
        conn.commit()
    else:
        conn.rollback()
    return cursor  

def show_tables():
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    cur = execute_query(query)
    result = cur.fetchall()
    i = 1
    for row in result:
        print(f"{i} : {row[0]}")
        i += 1

def display_attributes(name_table):
    cols = pd.read_sql_query(f"SELECT * from {name_table}", conn)
    attr = []
    for cols in cols.columns:
        attr.append(cols)
    print(attr) #affiche liste complète attributs

def getAttributes(t_name):
    cols = pd.read_sql_query(f"SELECT * from {t_name}", conn)
    attr = []
    for cols in cols.columns:
        attr.append(cols)
    return attr
    
def display_table(name_table, specified=False, num_rows=0):
    query = f"SELECT * FROM {name_table};"
    cur = execute_query(query)

    attr = getAttributes(name_table)
    attributes = " | ".join(attr)
    print("\n", attributes, "\n")

    if specified:
        result = cur.fetchmany(num_rows)
    else:
        result = cur.fetchall()
    
    for row in result:
        for i in range(len(row)):
            print(row[i], end=" | ")
        print("\n")
        # print(row) #print(row[1]) affiche 1re colonne de la table

def insert_value(name_table):
    attr = getAttributes(name_table)

    print("Number of values to insert: ", len(attr), "with values being: ", attr)
    attrStr = ",".join(attr)
    valToInsert = input("Entrez les valeurs à insérer séparées par des virgules : ")

    query = f"INSERT INTO {name_table}({attrStr}) VALUES ({valToInsert})"
    execute_query(query, True)

    conn.commit()

def del_value(name_table): #bien utiliser un attribut de type int pour delete sinon marche pas
    display_table(name_table)
    name = input("Entrez le nom de l'attribut de l'élément: ")
    value = input("Entrez la valeur de l'élément: ")
    
    query = f"DELETE FROM {name_table} WHERE {name} = {value}"
    execute_query(query, False)



conn = create_connection("testdb\GestionRegionale.db")
cursor = conn.cursor()


# show_tables()
# display_attributes("CLUB")

# insert_value("sqlite_sequence")
del_value("sqlite_sequence")
display_table("sqlite_sequence")
