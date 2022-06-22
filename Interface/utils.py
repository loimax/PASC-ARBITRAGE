import pandas as pd
import tkinter.messagebox as msg
import sqlite3
import os

def create_connection(db_file):
    """
    Create a database connection to a SQLite database
    :param: db_file :
    :return: conn : la connexion
    """
    if os.path.exists(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("The SQLite connection is opened")
            return conn
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)
    else:
        print("Error: Database not found")
        exit(1)

def close_connection(conn):
    if conn:
        conn.close()
        print("The SQLite connection is closed")
       
def execute_query(conn, cursor, query, del_ins=False):
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

def show_tables(conn, cursor):
    """
    Affiche les différentes tables du dossier
    :param: void
    :return: void
    """
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    cur = execute_query(conn, cursor, query)
    result = cur.fetchall()
    i = 1
    for row in result:
        print(f"{i} : {row[0]}")
        i += 1

def display_attributes(conn, cursor, name_table):
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

def getAttributes(conn, cursor, name_table): #t_name avant
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

def display_table(conn, cursor, name_table, specified=False, num_rows=0):
    """
    Affiche le contenu de la table spécifié en paramètre
    :param: name_table : nom de la table que l'on va afficher
    :param: specified :
    :param: num_rows :
    :param: spec_row :
    :return: void
    """
    query = f"SELECT * FROM {name_table};"
    cur = execute_query(conn, cursor, query)

    attr = getAttributes(conn, cursor, name_table)
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

def insert_entry(conn, cursor, name_table,list):
    """
    Insère une nouvelle entrée
    :param: name_table : nom de la table que l'on va modifier
    :param: list : les entrées de l'user sous forme de liste
    :return: void
    """
    attr = getAttributes(conn, cursor, name_table)
    attrStr = ",".join(attr)

    liste = ','.join("'" + item + "'" for item in list)

    query=f"INSERT INTO {name_table}({attrStr}) VALUES ({liste})"
    print(query)
    execute_query(conn, cursor, query, True)

def del_entry(conn, cursor, name_table, attribut, valeur):
    """
    Supprime une entrée de la table
    :param: name_table : nom de la table que l'on va modifier
    :return: void
    """
    query = f"DELETE FROM {name_table} WHERE {attribut} = '{valeur}'"
    execute_query(conn, cursor, query, True)#False, fonctionne avec True et non pas avec False
    # Le changement a été fait par Guillaume
    # Y'a un monde où j'avais juste pas compris comment l'utilisé ave 'True'
    # On hésite pas à me casser la gueule ou les gueules

def modify_entry(conn, cursor, name_table, list, id): #anciennement modify_value
    """
    Modifie un attribut d'une entrée de la table déjà existante
    :param: name_table : nom de la table que l'on va modifier
    :param: list : les entrées de l'user sous forme de liste
    :param: id : clé primaire de l'entrée modifier (on peut la modifier mais il nous la faut avant pour la trouver dans la database)
    :return: void
    """
    attr = getAttributes(conn, cursor, name_table)
    attr_id = attr[0]

    query = f"UPDATE {name_table} SET {attr[0]} = '{list[0]}' WHERE {attr_id} = '{id}'"
    execute_query(conn, cursor, query,True)

    i = 0
    for a in attr:
        query = f"UPDATE {name_table} SET {a} = '{list[i]}' WHERE {attr_id} = '{list[0]}'"
        execute_query(conn, cursor, query,True)
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


def creation_liste(conn, cursor, name_table, attribut):
    """
    Fonction qui renvoie sous forme de liste les attributs spécifié de chaque entrée d'une table 
    :param: name_table : nom de la table
    :param: attribut : liste des attributs qu'on veut dans notre liste (Sous la forme : ["a","b",...] OU ["a"])
    :return: liste : la liste des strings formées par notre demande
    """
    query = f"SELECT {attribut[0]}"
    print(len(attribut))
    if len(attribut)>1:
        i = 0
        for k in range(len(attribut)-1):
            i+=1
            query += f",{attribut[i]}"
            
    query +=f" FROM {name_table};"
    cur = execute_query(conn, cursor, query)

    result =cur.fetchall()

    
    liste = []
    for row in result:
        for i in range(len(row)+1-len(attribut)):
            JA_infos = ""
            for j in range(len(attribut)):
                JA_infos += f"{row[i+j]} "
            liste.append(JA_infos)
    print(liste)
    return(liste)

def getListRow(conn, cursor, name_table, list_attribut, list_valeur):
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

    cur = execute_query(conn, cursor, query)
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

def getValues(conn, cursor, name_table, attribute, id_base, id,):
    """
    Fonction qui renvoie la valeur de l'attribut demandé en trouvant la bonne entrée grâce à un attribut précisé 
    et la valeur connue
    :param: name_table : nom de la table
    :param: attribute : attribut de la valeur qu'on veut récupérer
    :param: id_base : nom de l'attribut qu'on connait de ce qu'on cherche
    :param: id : valeur de l'attribut qu'on connait
    :return: liste : renvoie la liste des valeurs de l'attribut recherché
    """
    # en cas de liste vide, on retourne directement la liste vide
    if id == [] : return id

    # cas "usuels" d'une liste non vide
    query = f"SELECT {attribute} FROM {name_table} WHERE {id_base}='{id[0]}'"
    i = 0
    for k in id:
        query+=f"OR {id_base}='{id[i]}'"
        i+=1
    cur = execute_query(conn, cursor, query)
    result = cur.fetchall()

    liste = []
    for row in result:
        liste.append(row[0])
    return liste

def getValuesFromList(list,x):
    """
    Cette fonction renvoie une liste d'un seul attribut des entrées d'une liste passé en paramètre
    :param: list : liste dont on va extraire 1 unique entrée de chaque sous-liste
    :param: x : entier qui indique le numéro de la case dont on veut extraire les données
    :return: liste : liste des entrées sélectionnées
    """
    liste = []
    for l in list:
        liste.append(l[x])
    return liste
  
def checkInsertModify(conn, cursor, name_table, liste, modify = False, nom = ""): 
    """
    on ne peut pas vérifier le type (text, int) 
    car les valeurs retournées par get() de tkinter sont en string par défaut, donc on peut mais ca prend 1000 lignes de code
    """
    dico = dict(name_table)
    keys = list(dico.keys())
    values = list(dico.values())
    i = 0
    if name_table == "CLUB":
        # print("La liste est : ", liste, " et les valeurs sont ", values, " pour les clés ", keys)
        for d in liste:
            if values[i][1] == "NULL" and len(d) == 0:
                liste[i] = "None"
            elif values[i][1] == "NOT NULL" and len(d) == 0:
                text = f"Erreur : Vous n'avez pas entré de valeur pour l'attribut '{keys[i]}' qui a comme contrainte '{values[i][1]}'; veuillez entrer une valeur"
                msg.showerror(title="Erreur : \n", message=text)
                return

            elif values[i][1] == "NOT NULL" and d == "None":
                text = f"Erreur : Vous avez entré la valeur 'None' pour l'attribut '{keys[i]}' qui a comme contrainte '{values[i][1]}' ; veuillez entrer une nouvelle valeur"
                msg.showerror(title="Erreur : \n", message=text)
                return
            i+=1
        if not modify:
            insert_entry(conn, cursor, name_table, liste)
        else:
            data = getListRow(conn, cursor, "CLUB", ["NomClub"], [nom])
            modify_entry(conn, cursor, name_table, liste, getID(data))

    elif name_table == "JA":
        for d in liste:
            if values[i][1] == "NULL" and len(d) == 0:
                liste[i] = "None"
            elif values[i][1] == "NOT NULL" and len(d) == 0:
                text = f"Erreur : Vous n'avez pas entré de valeur pour l'attribut '{keys[i]}' qui a comme contrainte '{values[i][1]}'; veuillez entrer une valeur"
                msg.showerror(title="Erreur : \n", message=text)
                return
            elif values[i][1] == "NOT NULL" and d == "None":
                text = f"Erreur : Vous avez entré la valeur 'None' pour l'attribut '{keys[i]}' qui a comme contrainte '{values[i][1]}' ; veuillez entrer une nouvelle valeur"
                msg.showerror(title="Erreur : \n", message=text)
                return
            i+=1
        if not modify:
            insert_entry(conn, cursor, name_table, liste)
        else:
            data = getListRow(conn, cursor, "JA", ["NumLic"], [nom])
            modify_entry(conn, cursor, name_table, liste, getID(data))

def alterTable(conn, cursor, name_table, attributes:list):
    print("len = ", len(attributes))
    
    query = f"ALTER TABLE {name_table} ADD {attributes[0]};"
    print(query)
    if len(attributes) > 1 :
        for i in range(len(attributes)-1):
            i+=1
            execute_query(conn, cursor, query, True)
            query = f"ALTER TABLE {name_table} ADD {attributes[i]};"
            print(query)
    
    execute_query(conn, cursor, query, True)

# fonction qui "concatène" NomClub et rgEquipe qui sont dans deux table différentes    
def join_table(conn,cursor,name_table,attributs,values):
    """
    
    :param: conn :
    :param: cursor :
    :param: name_table :
    :param: attributs :
    :return:
    """
    query = f"SELECT {values[0]}, {values[1]} FROM {name_table[0]} INNER JOIN {name_table[1]}"
    
def createViews(conn, cursor):
    """
    Création des vues
    """
    queryAllRencontres = """
        CREATE VIEW AllRencontres AS
        SELECT journee, DateRenc,  Eq1.division, Eq1.poule, 
            Club1.NomClub, Eq1.RangEq, 
            club2.NomClub, Eq2.RangEq, nomJA, prenomJA
        FROM  Rencontres R left join JA on R.JA = JA.NumLic, EquipeClub Eq1, CLUB Club1, 
            EquipeClub Eq2, CLUB Club2
        WHERE   R.NumEq1 = Eq1.NumEq
        AND   Eq1.numClub = Club1.numClub
        AND   R.NumEq2 = Eq2.numEq
        AND   Eq2.numClub = Club2.numClub
        ORDER BY journee, club1.NomClub, Eq1.RangEq
        """
    queryDonneesRencontres = """
        CREATE VIEW "DonneesRencontres" AS
        SELECT R.phase AS phase, R.Journee AS journee, EC1.Division AS division, EC1.Poule AS poule,
            C1.nomClub AS club1, EC1.RangEq AS equipe1, C2.nomClub AS club2, EC2.RangEq AS equipe2, 
            R.DateRenc AS jour, R.HeureRenc AS heure, C1.AdrClub AS adresseClub, C1.CPClub AS CPClub, C1.VilleClub AS villeClub,
            C1.Corres AS nomCorr, C1.TelCorr AS telCorr,
            JA.NumLic AS licenceJA, JA.NomJA AS nomJA, JA.PrenomJA AS prenomJA,
            CJA.NomClub AS clubJA, JA.AdrJA AS adresseJA, JA.CPJA AS CPJA, JA.VilleJA AS villeJA, JA.TelJA AS telJA, NumRenc
        FROM Rencontres R, CLUB C1, EquipeClub  EC1, CLUB C2, EquipeClub EC2, JA, CLUB CJA
        WHERE C1.Numclub = EC1.numclub
        AND   EC1.numeq = R.NumEq1
        AND   R.NumEq2 = EC2.numEq
        AND   EC2.numClub = C2.Numclub
        AND   JA.NumLic = R.JA
        AND   JA.ClubJA = CJA.NumClub
        """
    queryRecapIndivs = """
        CREATE VIEW RecapIndivs AS
        SELECT E2.NumEpreuve, NomEpreuve, DateEpr, TypeJA, nbJA, nomJA, PrenomJA, NumLic, AdrJA, CPJA, VilleJA, TelJA, Adjoint, Lieu, salle, CPLieu, Corres, telcorr, HeureEpr
        FROM 
        (SELECT E.NumEpreuve, NomEpreuve, DateEpr, HeureEpr, TypeJA, nbJA,  VilleClub AS Lieu, AdrClub as Salle, CPClub as CPLieu, Corres, telcorr
        FROM  Epreuves E LEFT JOIN CLUB ON CLUB.NumClub = E.lieu
        ) E2 
        LEFT JOIN 
        ( SELECT numepreuve, nomJA, PrenomJA, Numlic, AdrJA, CPJA, VilleJA, TelJA, Adjoint
            FROM Autresarbitrages AA, JA
            WHERE AA.Licarbitre = JA.numLic) A2
        ON E2.numepreuve = A2.NumEpreuve
        Order BY DateEpr
        """
    queryRecapitulatif = """
        CREATE VIEW Recapitulatif as
        SELECT Phase, journee, DateRenc, Eq1.division, Eq1.poule, 
            Club1.NomClub, Eq1.RangEq, 
            club2.NomClub, Eq2.RangEq, 
            nomJA, prenomJA, Club3.NomClub, telJA
        FROM  Rencontres R, EquipeClub Eq1, CLUB Club1, 
            EquipeClub Eq2, CLUB Club2,
            JA, Club Club3
        WHERE R.NumEq1 = Eq1.NumEq
        AND   Eq1.numClub = Club1.numClub
        AND   R.NumEq2 = Eq2.numEq
        AND   Eq2.numClub = Club2.numClub
        AND   R.JA = JA.NumLic
        AND   JA.ClubJA = Club3.numClub
        ORDER BY journee, DateRenc, Eq1.division
        """

    checkQueryAllRencontres = "DROP VIEW IF EXISTS AllRencontres;"
    checkQueryDonneesRencontres = "DROP VIEW IF EXISTS DonneesRencontres;"
    checkQueryRecapIndivs = "DROP VIEW IF EXISTS RecapIndivs;"
    checkQueryRecapitulatif = "DROP VIEW IF EXISTS Recapitulatif;" 
    execute_query(conn, cursor, checkQueryAllRencontres, True)
    execute_query(conn, cursor, checkQueryDonneesRencontres, True)
    execute_query(conn, cursor, checkQueryRecapIndivs, True)
    execute_query(conn, cursor, checkQueryRecapitulatif, True)

    execute_query(conn, cursor, queryAllRencontres, True)
    execute_query(conn, cursor, queryDonneesRencontres, True)
    execute_query(conn, cursor, queryRecapIndivs, True)
    execute_query(conn, cursor, queryRecapitulatif, True)

conn = create_connection("Interface/testdb/GestionRegionale.db")
cursor = conn.cursor()

createViews(conn, cursor)
display_table(conn, cursor, "")
# attributes = ["Année INTEGER NULL", "Phase INTEGER NOT NULL DEFAULT 1"]
# alterTable(conn, cursor, "EquipeClub", attributes)
# display_table(conn, cursor, "EquipeClub")

