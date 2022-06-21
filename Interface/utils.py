from tabnanny import check
import attr
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

    query = f"UPDATE {name_table} SET {attr[0]} = '{list[0]}' WHERE {attr_id} = '{id}'"
    execute_query(query,True)

    i = 0
    for a in attr:
        query = f"UPDATE {name_table} SET {a} = '{list[i]}' WHERE {attr_id} = '{list[0]}'"
        execute_query(query,True)
        i+=1


#vérifie si une valeur entrée en insert est du bon type (Null ou Not Null)
def dict(name_table):
    """
    :param:
    :return:
    """
    #dictionnaire : Attribut : list(type, null ou not null, default/Autoincrement)
    if name_table == "AutresArbitrages":
        autreArb = {'NumEpreuve':["int", "NOT NULL", "AUTOINCREMENT"], 'LicArbitre':["TEXT", "NULL"], 'Adjoint':["INTEGER", "NULL", "NON"]}
        return autreArb
    elif name_table == "CLUB":
        clubs = {"NumClub":["TEXT","NOT NULL"], "NomClub":["TEXT", "NOT NULL"], "VilleClub":["TEXT", "NOT NULL"], \
            "AdrClub":["TEXT", "NULL"], "CPClub":["TEXT","NULL"], "Corres":["TEXT","NULL"], "TelCorr":["TEXT", "NULL"]}
        return clubs
    elif name_table == "Epreuves":
        epreuves = {"NumEpreuve":["INTEGER", "NULL"], "NomEpreuve":["TEXT", "NOT NULL"], \
            "DateEpr":["TEXT", "NOT NULL"], "HeureEpr":["TEXT", "NULL"], "Lieu":["TEXT", "NULL"], \
                "TypeJA":["int", "NOT NULL", "3" ], "NbJA":["int", "NOT NULL", "1"]}
        return epreuves
    elif name_table == "EquipeClub":
        equipeClub = {"numEq":["int", "NOT NULL", "AUTOINCREMENT"], "numClub":["TEXT", "NOT NULL"], \
            "RangEq":["int", "NOT NULL"], "Masculin":["int", "NOT NULL"], "Division":["TEXT", "NOT NULL"], \
                "Poule":["TEXT", "NOT NULL"], "CorrEq":["TEXT", "NULL"]}
        return equipeClub
    elif name_table == "JA":
        ja = {"NumLic":["TEXT", "NOT NULL"], "NomJA":["TEXT", "NOT NULL"],"PrenomJA":["TEXT", "NOT NULL"],"ClubJA":["TEXT", "NOT NULL"],\
            "AdrJA":["TEXT", "NULL"],"CPJA":["TEXT", "NULL"], "VilleJA":["TEXT", "NULL"], "TelJA":["TEXT", "NOT NULL"]}
        return ja
    elif name_table == "Rencontres":
        rencontres = {"NumRenc":["int", "NOT NULL", "AUTOINCREMENT"], "NumEq1":["int", "NOT NULL"], \
            "NumEq2":["int", "NOT NULL"], "Phase":["int", "NOT NULL"], "Journee":["int", "NOT NULL"], \
                "DateRenc":["TEXT", "NOT NULL"], "HeureRenc":["TEXT", "NOT NULL"], "JA":["TEXT", "NULL"]}
        return rencontres
    # else :
    #     liste = [autreArb, clubs, epreuves, equipeClub, ja, rencontres]
    #     return liste


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

def getListRow(name_table, list_attribut, list_valeur):
    """
    Envoie les entrées correspondant à la (ou les) spécification(s) sous forme de liste;
    exemples : getListRow("EquipeClub",["Division","Poule","RangEq","Masculin","NumEq"],["R3","G","1","0","107"])
               getListRow("CLUB",["VilleClub"],["Bourges"])
    :param: name_table : nom de la table
    :param: list_attribut : liste d'attribut qu'on veut spécifier
    :param: list_valeur : liste de valeur, avec une valeur par attribut
    :return: liste (cas une seule entrée) : une liste des valeurs
    :return: liste (cas plusieurs entrées) : une liste de liste des valeurs de chaque entrée
    """
    query = f'SELECT * FROM {name_table} WHERE "{list_attribut[0]}" = "{list_valeur[0]}"'
    if len(list_attribut) > 1 :
        for i in range(len(list_attribut)-1):
            i+=1
            query += f'AND "{list_attribut[i]}" = "{list_valeur[i]}" '
    query += ';'

    cur = execute_query(query)
    result = cur.fetchall()
    
    if len(result) > 1 :
        liste = []
        for row in result:
            liste.append(row)        
    else:
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

def checkInsert(name_table, liste): 
    """
    on ne peut pas vérifier le type (text, int) 
    car les valeurs retournées par get() de tkinter sont en string par défaut, donc on peut mais ca prend 1000 lignes de code
    """
    dico = dict(name_table)
    values = list(dico.values())
    i = 0
    for d in liste:
        if values[i][1] == "NULL" and len(d) == 0:
            liste[i] = "NULL"
        elif (values[i][1] == "NOT NULL" and len(d) == 0):
            print(f"Test numéro 1 pour d={d} avec pour valeur {values[i][1]}")
            #il faut une alrte box ici je personaliserai le texte dedans
            return
        elif values[i][1] == "NOT NULL" and d == "NULL":
            print(f"Test numéro 2 pour d={d}")
            return
        i+=1
    insert_entry(name_table, liste)



conn = create_connection("Interface/testdb/GestionRegionale.db")
cursor = conn.cursor()



    