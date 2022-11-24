from tkinter import *
import os

from utils import *

class JA():
    def __init__(self):
        #creer une fenetre
        self.main_window = Tk()
        #donner un titre a la fenetre
        self.main_window.title("JA")

        #donner une taille a la fenetre
        #taille de la fenetre s'adapte a la taille de l'ecran
        self.main_window.geometry("{0}x{1}+0+0".format(self.main_window.winfo_screenwidth(), self.main_window.winfo_screenheight()))

        #connexion à la base de données
        self.conn = create_connection("Interface/testdb/GestionRegionale.db")
        self.cursor = self.conn.cursor()
        self.setup()
        self.main_window.attributes('-fullscreen', True)
        self.main_window.mainloop()

    def update(self,data):
        #clear the listbox
        self.JA_list.delete(0,END)

        #ajpouter les JA dans la listbox
        for item in data:
            self.JA_list.insert(END, item)

    #afficher le JA séléctionné
    def fillout(self,e):
        self.entry_JA.delete(0, END)
        self.entry_JA.insert(0, self.JA_list.get(ANCHOR))

    #créer fonction entrée vs liste de JA
    def check(self,e):
        #grab what typed
        typed = self.entry_JA.get()

        if typed == '':
            data = self.liste_JA
        else:
            data = []
            for item in self.liste_JA:
                if typed.lower() in item.lower():
                    data.append(item)

        self.update(data)

    
    #faire une fonction qui ouvre un formulaire pour ajouter un JA lorque on clique sur le bouton
    def func_add_JA(self):
        clubs = dict("CLUB")
        values = list(clubs.values())
        i = 0
        #créer une fenetre
        self.add_JA = Tk()
        #donner un titre a la fenetre
        self.add_JA.title("Ajouter un JA")
        #donner une taille a la fenetre
        self.add_JA.geometry("400x250")
        #couleur de fond de la fenetre
        self.add_JA.configure(background='#DADAD7')
        #créer une zone de texte pour les noms des JAs
        entry_numero_JA = Entry(self.add_JA, width=30)
        entry_numero_JA.grid(row=1, column=2)
        #créer une zone de texte pour les noms des JAs
        entry_nom_JA = Entry(self.add_JA, width=30)
        entry_nom_JA.grid(row=2, column=2)
        #créer une zone de texte pour les noms des JAs
        entry_prenom_JA = Entry(self.add_JA, width=30)
        entry_prenom_JA.grid(row=3, column=2)
        #créer une zone de texte pour les noms des JAs
        entry_club_JA = Entry(self.add_JA, width=30)
        entry_club_JA.grid(row=4, column=2)
        #créer une zone de texte pour les noms des JAs
        entry_adresse_JA = Entry(self.add_JA, width=30)
        entry_adresse_JA.grid(row=5, column=2)
        #créer une zone de texte pour les noms des JAs
        entry_cp_JA = Entry(self.add_JA, width=30)
        entry_cp_JA.grid(row=6, column=2)
        #créer une zone de texte pour les noms des JAs
        entry_ville_JA = Entry(self.add_JA, width=30)
        entry_ville_JA.grid(row=7, column=2)
        #créer une zone de texte pour le Tel du JA
        entry_tel_JA = Entry(self.add_JA, width=30)
        entry_tel_JA.grid(row=8, column=2)
        #afficher les titres des zones de texte

        if values[i][1] == "NOT NULL":
            text = "*"
        label_numero = Label(self.add_JA, text=f"Numéro de Licence du JA : {text}")
        label_numero.grid(row=1, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_nomJA = Label(self.add_JA, text=f"Nom du JA : {text}")
        label_nomJA.grid(row=2, column=1)
        i+=1
        text = ""
        
        if values[i][1] == "NOT NULL":
            text = "*"
        label_prenom_JA = Label(self.add_JA, text=f"Prenom : {text}")
        label_prenom_JA.grid(row=3, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_clubJA = Label(self.add_JA, text=f"club : {text}")
        label_clubJA.grid(row=4, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_adresse_JA = Label(self.add_JA, text=f"Adresse : {text}")
        label_adresse_JA.grid(row=5, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_cp = Label(self.add_JA, text=f"cp : {text}")
        label_cp.grid(row=6, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_ville = Label(self.add_JA, text=f"Ville : {text}")
        label_ville.grid(row=7, column=1)
        i+=1
        text = "*"

        label_tel = Label(self.add_JA, text=f"Tel : {text}")
        label_tel.grid(row=8, column=1)

        #créer un bouton pour valider les données
        button_valider = Button(self.add_JA, text="Valider",command=lambda : [self.add_JA_data(entry_numero_JA,entry_nom_JA,entry_prenom_JA,entry_club_JA,entry_adresse_JA,entry_cp_JA,entry_ville_JA,entry_tel_JA)])
        button_valider.grid(row=9, column=2)
          #ajouter un texte pour indiquer que les champs sont obligatoires
        label_obligatoire = Label(self.add_JA, text="* : Champs obligatoires")
        label_obligatoire.grid(row=10, column=2)
    #recuperer les données du formulaire
    def add_JA_data(self,num,nom,prenom,club,adresse,cp,ville,tel):
        numero_JA = num.get()
        nom_JA = nom.get()
        prenom_JA = prenom.get()
        club_JA = club.get()
        adresse_JA = adresse.get()
        cp_JA = cp.get()
        ville_JA = ville.get()
        tel_JA = tel.get()
        # mettre les elements dans une liste
        data = [numero_JA, nom_JA, prenom_JA, club_JA, adresse_JA, cp_JA, ville_JA, tel_JA]

        checkInsertModify(self.conn, self.cursor, "JA", data)
        # insert_entry("JA", data)
        self.add_JA.destroy()
    
    def supprimer_JA(self):
        nom = self.JA_list.get(ANCHOR)
        #On coupe la string "Prénom Nom NumLicence " pour avoir seulement NumLicence
        Num_Licence = nom.rsplit(' ',2)[1]
        del_entry(self.conn, self.cursor, "JA", "NumLic", Num_Licence)
        update_tables(self.conn, self.cursor, "JA")
        #update(liste_JAs)

    def rafraichir(self):
        self.main_window.destroy()
        update_tables(self.conn, self.cursor, "JA")
        close_connection(self.conn)
        JA()
        # os.system("python Interface/JA.py")

    def modifier_JA(self):
        nom = self.JA_list.get(ANCHOR)
        #On coupe la string "Prénom Nom NumLicence " pour avoir seulement NumLicence
        Num_Licence = nom.rsplit(' ',2)[1]
        #on ouvre une fenetre
        modif_JA = Tk()
        #on donne un titre a la fenetre
        modif_JA.title("Modifier un JA")
        #on donne une taille a la fenetre
        modif_JA.geometry("400x250")
        #on crée un formulaire ou on affiche les données du JA séléctionné
        label_numero = Label(modif_JA, text="Numéro de Licence du JA : *")
        label_numero.grid(row=1, column=1)
        label_nomJA = Label(modif_JA, text="Nom du JA : *")
        label_nomJA.grid(row=2, column=1)
        label_prenom_JA = Label(modif_JA, text="Prénom du JA : *")
        label_prenom_JA.grid(row=3, column=1)
        label_clubJA = Label(modif_JA, text="Club du JA: *")
        label_clubJA.grid(row=4, column=1)
        label_adresse_JA = Label(modif_JA, text="adresse :")
        label_adresse_JA.grid(row=5, column=1)
        label_cp = Label(modif_JA, text="CP :")
        label_cp.grid(row=6, column=1)
        label_ville = Label(modif_JA, text="Ville :")
        label_ville.grid(row=7, column=1)
        label_tel = Label(modif_JA, text="TelJA: *")
        label_tel.grid(row=8, column=1)
        #on recupere les données du JA séléctionné
        data = getListRow(self.conn, self.cursor, "JA", ["NumLic"], [Num_Licence])
        #on les affiche dans le formulaire
        entry_numero_JA = Entry(modif_JA, width=30)
        entry_numero_JA.grid(row=1, column=2)
        entry_numero_JA.insert(END, data[0])
        entry_nom_JA = Entry(modif_JA, width=30)
        entry_nom_JA.grid(row=2, column=2)
        entry_nom_JA.insert(END, data[1])
        entry_prenom_JA = Entry(modif_JA, width=30)
        entry_prenom_JA.grid(row=3, column=2)
        entry_prenom_JA.insert(END, data[2])
        entry_club_JA = Entry(modif_JA, width=30)
        entry_club_JA.grid(row=4, column=2)
        entry_club_JA.insert(END, data[3])
        entry_adresse_JA = Entry(modif_JA, width=30)
        entry_adresse_JA.grid(row=5, column=2)
        entry_adresse_JA.insert(END, data[4])
        entry_cp_JA = Entry(modif_JA, width=30)
        entry_cp_JA.grid(row=6, column=2)
        entry_cp_JA.insert(END, data[5])
        entry_ville_JA = Entry(modif_JA, width=30)
        entry_ville_JA.grid(row=7, column=2)
        entry_ville_JA.insert(END, data[6])
        entry_tel_JA = Entry(modif_JA, width=30)
        entry_tel_JA.grid(row=8, column=2)
        entry_tel_JA.insert(END, data[7])

        #mettre les elements dans une liste
        #mod = [entry_numero_JA, entry_nom_JA, entry_prenom_JA, entry_club_JA, entry_adresse_JA, entry_cp_JA, entry_ville_JA]
        #on crée un bouton pour valider les données
        button_valider = Button(modif_JA, text="Valider", command = lambda : [self.modif_JA_data(entry_numero_JA,entry_nom_JA,entry_prenom_JA,entry_club_JA,entry_adresse_JA,entry_cp_JA,entry_ville_JA,entry_tel_JA,Num_Licence), update_tables(self.conn, self.cursor, "JA"), modif_JA.destroy()])
        button_valider.grid(row=9, column=2)
          #ajouter un texte pour indiquer que les champs sont obligatoires
        label_obligatoire = Label(modif_JA, text="* : Champs obligatoires")
        label_obligatoire.grid(row=10, column=2)
        #,X
        # button_valider = Button(add_JA, text="Valider",command=lambda : [add_JA_data(), update(liste_JAs)])
        #button_valider.grid(row=8, column=2)
        
    def modif_JA_data(self,num,nom,prenom,club,adresse,cp,ville,tel, Num_Licence):
        numero_JA = num.get()
        nom_JA = nom.get()
        prenom_JA = prenom.get()
        club_JA = club.get()
        adresse_JA = adresse.get()
        cp_JA = cp.get()
        ville_JA = ville.get()
        tel_JA = tel.get()
        # mettre les elements dans une liste
        a = [numero_JA, nom_JA, prenom_JA, club_JA, adresse_JA, cp_JA, ville_JA, tel_JA]
        update_tables(self.conn, self.cursor, "JA")
        checkInsertModify(self.conn, self.cursor, "JA", a, True, Num_Licence)
        

    def setup(self):
        #créer 3 boutons pour les JAs : modifier ajouter supprimer
        title = Label(self.main_window, text="Liste des Juges Arbitres :", font=('Arial', 24))
        bouton_modifier = Button(self.main_window, text="Modifier", fg='#000000', font=('Arial', 10),command=self.modifier_JA)
        bouton_ajouter = Button(self.main_window, text="Ajouter", fg='#000000', font=('Arial', 10),command=self.func_add_JA)
        bouton_supprimer = Button(self.main_window, text="Supprimer", fg='#000000', font=('Arial', 10), command=lambda : [self.supprimer_JA()])
        bouton_rafraichir = Button(self.main_window, text="Rafraichir", fg='#000000', font=('Arial', 10, 'bold'),command=self.rafraichir)
        bouton_retour = Button(self.main_window, text="Retour", command=self.retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_quitter = Button(self.main_window, text="Quitter", command=self.quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        self.entry_JA = Entry(self.main_window, font=("Arial", 20))
        self.JA_list = Listbox(self.main_window, width=50)
        
        title.place(x = 0, y = 0)
        bouton_modifier.place(x = 0, y = 0)
        bouton_ajouter.place(x = 0, y = 0)
        bouton_supprimer.place(x = 0, y = 0)
        bouton_rafraichir.place(x = 0, y = 0)
        bouton_retour.place(x = 0, y = 0)
        bouton_quitter.place(x = 0, y = 0)
        self.entry_JA.place(x = 0, y = 0)
        self.JA_list.place(x = 0, y = 0)

        #display_attributes(self.conn,self.cursor,"JA")
        self.liste_JA = creation_liste(self.conn, self.cursor, "JA", ["PrenomJA","NomJA","NumLic"])
        # liste_JA = ["Nom 1", "Nom 2", "Nom 3", "Nom 4", "Nom 5", "Nom 6", "Nom 7", "Nom 8", "Nom 9", "Nom 10", "Nom 11", "Nom 12", "Nom 13", "Nom 14", "Nom 15", "Nom 16", "Nom 17", "Nom 18", "Nom 19", "Nom 20", "Nom 21", "Nom 22", "Nom 23", "Nom 24", "Nom 25", "Nom 26", "Nom 27", "Nom 28", "Nom 29", "Nom 30", "Nom 31", "Nom 32", "Nom 33", "Nom 34", "Nom 35", "Nom 36"]
        #Ajouter JA dans la liste
        self.update(self.liste_JA)

        #afficher le JA selectionné
        self.JA_list.bind("<<ListboxSelect>>", self.fillout)

        #create a binding to the entry box
        self.entry_JA.bind("<KeyRelease>", self.check)

        
        update_tables(self.conn, self.cursor, "JA", True)
        #afficher la fenetre
        
        
        self.main_window.update()

        title.place(x = self.main_window.winfo_width()/2 - title.winfo_width()/2, y = 100)
        bouton_ajouter.place(x = self.main_window.winfo_width()/2 + self.entry_JA.winfo_width()/2 + 50, y = 250 + ((self.JA_list.winfo_height() - 3 * bouton_ajouter.winfo_height())/4))
        bouton_supprimer.place(x = self.main_window.winfo_width()/2 + self.entry_JA.winfo_width()/2 + 50, y = 250 + (2 * (self.JA_list.winfo_height() - 3 * bouton_ajouter.winfo_height())/4) + bouton_ajouter.winfo_height())
        bouton_modifier.place(x = self.main_window.winfo_width()/2 + self.entry_JA.winfo_width()/2 + 50, y = 250 + (3 * (self.JA_list.winfo_height() - 3 * bouton_ajouter.winfo_height())/4) + 2 * bouton_ajouter.winfo_height())
        bouton_rafraichir.place(x = self.main_window.winfo_width()/2 - bouton_rafraichir.winfo_width()/2, y = 450)
        bouton_retour.place(x = 0.02*self.main_window.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
        bouton_quitter.place(x = 0.98*self.main_window.winfo_width()-bouton_retour.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
        self.entry_JA.place(x = self.main_window.winfo_width()/2 - self.entry_JA.winfo_width()/2, y = 200)
        self.JA_list.place(x = self.main_window.winfo_width()/2 - self.JA_list.winfo_width()/2, y = 250)

    def retour(self):
        self.main_window.destroy()
        update_tables(self.conn, self.cursor, "JA")

        os.system("python Interface/main.py")

    def quitter(self):
        close_connection(self.conn)
        self.main_window.destroy()