import pandas as pd
import sqlite3
import os

def create_connection(db_file):
    """ 
    Create a database connection to a SQLite database
    :param: db_file :
    :return: conn : la connexion
    """
    if os.path.exists(db_file):
        conn = sqlite3.connect(db_file)
        return conn
    else:
        print("Error: Database not found")
        exit(1)

def execute_query(query, del_ins=False):
    """
    Execute la requête passé en paramètre
    :param: query : la requête écrite en demande SQLite
    :param: del_ins : 
    :return: cursor :
    """
    cursor.execute(query)
    if del_ins:
        conn.commit()
    else:
        conn.rollback()
    return cursor  

def show_tables():
    """
    Affiche les différentes tables du dossier
    :param: void
    :return: void
    """
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    cur = execute_query(query)
    result = cur.fetchall()
    i = 1
    for row in result:
        print(f"{i} : {row[0]}")
        i += 1

def display_attributes(name_table):
    """
    Affiche la liste des attributs d'une table
    :param: name_table : nom de la table
    :return: void
    """
    cols = pd.read_sql_query(f"SELECT * from {name_table}", conn)
    attr = []
    for cols in cols.columns:
        attr.append(cols)
    print(attr) #affiche liste complète attributs

def getAttributes(name_table): #t_name avant
    """
    Renvoie la liste des attributs d'une table
    :param: name_table : nom de la table
    :return: attr : un tableau des attributs
    """
    cols = pd.read_sql_query(f"SELECT * from {name_table}", conn)
    attr = []
    for cols in cols.columns:
        attr.append(cols)
    return attr
    
def display_table(name_table, specified=False, num_rows=0, spec_row=""):
    """
    Affiche le contenu de la table spécifié en paramètre
    :param: name_table : nom de la table que l'on va afficher
    :param: specified :
    :param: num_rows :
    :param: spec_row :
    :return: void
    """
    query = f"SELECT * FROM {name_table};"
    cur = execute_query(query)

    attr = getAttributes(name_table)
    attributes = " | ".join(attr)
    print("\n", attributes, "\n")

    if specified:
        result = cur.fetchmany(num_rows)
    else:
        result = cur.fetchall()


    if spec_row != "":
        for row in result:
            if row[0] == spec_row: #check id club pour l'instant
                for i in range(len(row)):
                    print(row[i], end=" | ")
            break
             
    for row in result:
        for i in range(len(row)):
            print(row[i], end=" | ")
        print("\n")
        # print(row) #print(row[1]) affiche 1re colonne de la table

def insert_entry(name_table,list):
    """
    Insère une nouvelle entrée 
    :param: name_table : nom de la table que l'on va modifier
    :param: list : les entrées de l'user sous forme de liste
    :return: void
    """
    attr = getAttributes(name_table)
    attrStr = ",".join(attr)

    liste = ','.join("'" + item + "'" for item in list)
    
    query=f"INSERT INTO {name_table}({attrStr}) VALUES ({liste})"
    print(query)
    execute_query(query, True)
    conn.commit()

def del_entry(name_table, attribut, valeur): 
    """
    Supprime une entrée de la table
    :param: name_table : nom de la table que l'on va modifier
    :return: void
    """
    query = f"DELETE FROM {name_table} WHERE {attribut} = '{valeur}'"
    execute_query(query, True)#False, fonctionne avec True et non pas avec False
    # Le changement a été fait par Guillaume
    # Y'a un monde où j'avais juste pas compris comment l'utilisé ave 'True'
    # On hésite pas à me casser la gueule ou les gueules

def modify_entry(name_table, list, id): #anciennement modify_value
    """
    Modifie un attribut d'une entrée de la table déjà existante
    :param: name_table : nom de la table que l'on va modifier
    :param: list : les entrées de l'user sous forme de liste
    :param: id : clé primaire de l'entrée modifier (on peut la modifier mais il nous la faut avant pour la trouver dans la database)
    :return: void
    """
    attr = getAttributes(name_table)
    attr_id = attr[0]

    query = f"UPDATE {name_table} SET {attr[0]} = '{list[0]}' WHERE {attr_id} = {id}"
    print(query)
    execute_query(query,True)

    i = 0
    for a in attr:
        query = f"UPDATE {name_table} SET {a} = '{list[i]}' WHERE {attr_id} = {list[0]}"
        print(query)
        execute_query(query,True)
        i+=1


#vérifie si une valeur entrée en insert est du bon type (Null ou Not Null)
def checkValueType(name_table): 
    """
    
    :param:
    :return: 
    """
    pass

def creation_liste(name_table, attribut):
    """
    
    :param: name_table : nom de la table
    :param: attribut : 
    :return: 
    """
    query = f"SELECT {attribut} FROM {name_table};"
    cur = execute_query(query)

    result =cur.fetchall()


    liste = []
    for row in result:
        for i in range(len(row)):
            liste.append(row[i])

    return(liste)

def getListRow(name_table, attribut, valeur):
    """
    
    :param: name_table : nom de la table
    :param: attribut :  
    :param: valeur :
    :return: 
    """
    query = f'SELECT * FROM {name_table} WHERE "{attribut}" = "{valeur}";'
    cur = execute_query(query)
    result = cur.fetchall()

    liste = []
    for row in result:
        for i in range(len(row)):
            liste.append(row[i])
    print(liste)
    return(liste)

def getID(list):
    """
    Fonction qui retourne la clé primaire d'une entrée de la table
    :param: list : une entrée de la table
    :return: list[0] : la 1ere valeur de l'entrée de la table (supposément la clé primaire)
    """
    return list[0]

conn = create_connection("Interface/testdb/GestionRegionale.db")
cursor = conn.cursor()

display_table("CLUB")
l1 = ["81","G","","","","","18"]
#insert_entry("CLUB",l1)
display_table("CLUB")
l = ["906","Allo","Dilo","78","lou","","99071"]
modify_entry("CLUB",l,getID(l1))
display_table("CLUB")

