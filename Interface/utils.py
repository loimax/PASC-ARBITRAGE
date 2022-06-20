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

def insert_entry(name_table): #anceinnement insert_value
    """
    Insère une nouvelle entrée 
    :param: name_table : nom de la table que l'on va modifier
    :return: void
    """
    attr = getAttributes(name_table)

    print("Number of values to insert: ", len(attr), "with values being: ", attr)
    attrStr = ",".join(attr)
    valToInsert = input("Entrez les valeurs à insérer séparées par des virgules : ")
    # Il faut encadrer de ' ' nos valeurs ajoutées
    # exemple : je veux insérer a et b car on a deux attributs;
    # on écrit dans input : 'a','b'
    query = f"INSERT INTO {name_table}({attrStr}) VALUES ({valToInsert})"
    execute_query(query, True)

    conn.commit()

def del_entry(name_table): #anciennement del_value #bien utiliser un attribut de type int pour delete sinon marche pas
    """
    Supprime une entrée de la table
    :param: name_table : nom de la table que l'on va modifier
    :return: void
    """
    display_table(name_table)
    name = input("Entrez le nom de l'attribut de l'élément: ")
    value = input("Entrez la valeur de l'élément: ")
    
    query = f"DELETE FROM {name_table} WHERE {name} = {value}"
    execute_query(query, True)#False, fonctionne avec True et non pas avec False
    # Le changement a été fait par Guillaume
    # Y'a un monde où j'avais juste pas compris comment l'utilisé ave 'True'
    # On hésite pas à me casser la gueule

def modify_entry(name_table): #anciennement modify_value
    """
    Modifie un attribut d'une entrée de la table déjà existante
    :param: name_table : nom de la table que l'on va modifier
    :return: void
    """
    display_table(name_table)
    id = input("Entrez l'ID de la ligne à modifier : ")
    attr = input("Entrez l'attribut que vous voulez changer : ")
    value = input("Entrez la nouvelle valeur : ")

    # Pour l'instant fonction spécifique à la table "JA"
    # Il faut changer NumLic dans la query pour qu'elle prenne toujours l'ID de la table passé en paramêtre
    query = f"UPDATE {name_table} SET {attr} = {value} WHERE NumLic = {id}"
    execute_query(query,True)


#vérifie si une valeur entrée en insert est du bon type (Null ou Not Null)
def checkValueType(name_table): 
    """
    
    :param:
    :return: 
    """
    pass


def creation_liste_club(name_table="CLUB"):
    query = f"SELECT NomClub FROM {name_table};"
    cur = execute_query(query)

    result =cur.fetchall()


    liste_club = []
    for row in result:
        for i in range(len(row)):
            liste_club.append(row[i])

    return(liste_club)


conn = create_connection("Interface/testdb/GestionRegionale.db")
cursor = conn.cursor()