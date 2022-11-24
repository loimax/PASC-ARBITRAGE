from tkinter import *
import os
from utils import *

class Clubs():
    
    def __init__(self):
        self.conn = create_connection("Interface/testdb/GestionRegionale.db")
        self.cursor = self.conn.cursor()
        update_tables(self.conn, self.cursor, "CLUB", True)
        #créer une fenetre
        self.main_window = Tk()
        #donner un titre a la club
        self.main_window.title("Clubs")
        self.main_window.attributes('-fullscreen', True)

        #donner une taille a la club
        #club.geometry("1920x1080")
        #taille de la club s'adapte a la taille de l'ecran
        self.main_window.geometry("{0}x{1}+0+0".format(self.main_window.winfo_screenwidth(), self.main_window.winfo_screenheight()))

        title = Label(self.main_window, text="Liste des Clubs :", font=('Arial', 24))
        # créer 3 boutons pour les clubs : modifier ajouter supprimer
        bouton_modifier = Button(self.main_window, text="Modifier", fg='#000000', font=('Arial', 10, 'bold'), command=self.modifier_club)
        bouton_ajouter = Button(self.main_window, text="Ajouter", fg='#000000', font=('Arial', 10, 'bold'), command=self.add_club)
        bouton_supprimer = Button(self.main_window, text="Supprimer", fg='#000000', font=('Arial', 10, 'bold'),command=self.supprimer_club)
        bouton_rafraichir = Button(self.main_window, text="Rafraichir", fg='#000000', font=('Arial', 10, 'bold'),command=self.rafraichir)
        bouton_retour = Button(self.main_window, text="Retour", command=self.retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_quitter = Button(self.main_window, text="Quitter", command=self.quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        self.entry_clubs = Entry(self.main_window, font=("Helvetica", 20))
        self.main_window_list = Listbox(self.main_window, width=50)

        title.place(x = 0, y = 0)
        bouton_modifier.place(x = 0, y = 0)
        bouton_ajouter.place(x = 0, y = 0)
        bouton_supprimer.place(x = 0, y = 0)
        bouton_rafraichir.place(x = 0, y = 0)
        bouton_retour.place(x = 0, y = 0)
        bouton_quitter.place(x = 0, y = 0)
        self.entry_clubs.place(x = 0, y = 0)
        self.main_window_list.place(x = 0, y = 0)

        # créer une liste de clubs
        self.liste_clubs = creation_liste(self.conn, self.cursor, "CLUB", ["NomClub"])

        # afficher le club selectionné
        self.main_window_list.bind("<<ListboxSelect>>", self.fillout)

        # create a binding to the entry box
        self.entry_clubs.bind("<KeyRelease>", self.check)

        # Ajouter club selectionne dans listbox
        self.update_listbox(self.liste_clubs)
        self.liste_clubs = creation_liste(self.conn, self.cursor, "CLUB", ["NomClub"])

        self.main_window.update()
        title.place(x = self.main_window.winfo_width()/2 - title.winfo_width()/2, y = 100)
        bouton_ajouter.place(x = self.main_window.winfo_width()/2 + self.entry_clubs.winfo_width()/2 + 50, y = 250 + ((self.main_window_list.winfo_height() - 3 * bouton_ajouter.winfo_height())/4))
        bouton_supprimer.place(x = self.main_window.winfo_width()/2 + self.entry_clubs.winfo_width()/2 + 50, y = 250 + (2 * (self.main_window_list.winfo_height() - 3 * bouton_ajouter.winfo_height())/4) + bouton_ajouter.winfo_height())
        bouton_modifier.place(x = self.main_window.winfo_width()/2 + self.entry_clubs.winfo_width()/2 + 50, y = 250 + (3 * (self.main_window_list.winfo_height() - 3 * bouton_ajouter.winfo_height())/4) + 2 * bouton_ajouter.winfo_height())
        bouton_rafraichir.place(x = self.main_window.winfo_width()/2 - bouton_rafraichir.winfo_width()/2, y = 450)
        bouton_retour.place(x = 0.02*self.main_window.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
        bouton_quitter.place(x = 0.98*self.main_window.winfo_width()-bouton_retour.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
        self.entry_clubs.place(x = self.main_window.winfo_width()/2 - self.entry_clubs.winfo_width()/2, y = 200)
        self.main_window_list.place(x = self.main_window.winfo_width()/2 - self.entry_clubs.winfo_width()/2, y = 250)

        self.main_window.mainloop()


    #uptade de la liste des clubs
    def update_listbox(self, data):
        #clear the listbox
        self.main_window_list.delete(0, END)

        #ajpouter les clubs dans la listbox
        for item in data:
            self.main_window_list.insert(END, item)

    #afficher le club séléctionné
    def fillout(self, e):
        self.entry_clubs.delete(0, END)
        self.entry_clubs.insert(0, self.main_window_list.get(ANCHOR))

    #créer fonction entrée vs liste de clubs
    def check(self, e):
        #grab what typed
        typed = self.entry_clubs.get()

        if typed == '':
            data = self.liste_clubs
        else:
            data = []
            for item in self.liste_clubs:
                if typed.lower() in item.lower():
                    data.append(item)

        self.update_listbox(data)

    #faire une fonction qui ouvre un formulaire pour ajouter un club lorque on clique sur le bouton
    def add_club(self):
        clubs = dict("CLUB")
        values = list(clubs.values())
        i = 0
        #créer une fenetre
        add_club = Tk()
        #donner un titre a la fenetre
        add_club.title("Ajouter un club")
        #donner une taille a la fenetre
        add_club.geometry("400x200")
        #couleur de fond de la fenetre
        add_club.configure(background='#DADAD7')
        #créer une zone de texte pour les noms des clubs
        entry_numero_club = Entry(add_club, width=30)
        entry_numero_club.grid(row=1, column=2)
        #créer une zone de texte pour les noms des clubs
        entry_nom_club = Entry(add_club, width=30)
        entry_nom_club.grid(row=2, column=2)
        #créer une zone de texte pour les noms des clubs
        entry_ville_club = Entry(add_club, width=30)
        entry_ville_club.grid(row=3, column=2)
        #créer une zone de texte pour les noms des clubs
        entry_adresse_club = Entry(add_club, width=30)
        entry_adresse_club.grid(row=4, column=2)
        #créer une zone de texte pour les noms des clubs
        entry_cp_club = Entry(add_club, width=30)
        entry_cp_club.grid(row=5, column=2)
        #créer une zone de texte pour les noms des clubs
        entry_correspondant_club = Entry(add_club, width=30)
        entry_correspondant_club.grid(row=6, column=2)
        #créer une zone de texte pour les noms des clubs
        entry_tel_club = Entry(add_club, width=30)
        entry_tel_club.grid(row=7, column=2)
        #afficher les titres des zones de texte
        if values[i][1] == "NOT NULL":
            text = "*"
        label_numero = Label(add_club, text=f"Numéro de club : {text}")
        label_numero.grid(row=1, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_nomclub = Label(add_club, text=f"Nom du club : {text}")
        label_nomclub.grid(row=2, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_ville_club = Label(add_club, text=f"Ville : {text}")
        label_ville_club.grid(row=3, column=1)
        i+=1
        text = ""
        if values[i][1] == "NOT NULL":
            text = "*"
        label_adresseclub = Label(add_club, text=f"Adresse : {text}")
        label_adresseclub.grid(row=4, column=1)
        i+=1
        text = ""
        if values[i][1] == "NOT NULL":
            text = "*"
        label_cp_club = Label(add_club, text=f"CP : {text}")
        label_cp_club.grid(row=5, column=1)
        i+=1
        text = ""
        if values[i][1] == "NOT NULL":
            text = "*"
        label_correspondant = Label(add_club, text=f"Correspondant : {text}")
        label_correspondant.grid(row=6, column=1)
        i+=1
        text = ""
        if values[i][1] == "NOT NULL":
            text = "*"
        label_Tel = Label(add_club, text=f"Téléphone : {text}")
        label_Tel.grid(row=7, column=1)
        text = ""
        #recuperer les données du formulaire
        def add_club_data():
            numero_club = entry_numero_club.get()
            nom_club = entry_nom_club.get()
            ville_club = entry_ville_club.get()
            adresse_club = entry_adresse_club.get()
            cp_club = entry_cp_club.get()
            correspondant_club = entry_correspondant_club.get()
            tel_club = entry_tel_club.get()
            # mettre les elements dans une liste
            print(numero_club, nom_club, ville_club, adresse_club, cp_club, correspondant_club, tel_club)
            data = [numero_club, nom_club, ville_club, adresse_club, cp_club, correspondant_club, tel_club]

            checkInsertModify(self.conn, self.cursor, "CLUB", data)
            add_club.destroy()




        #créer un bouton pour valider les données
        button_valider = Button(add_club, text="Valider",command=lambda : [add_club_data()])
        button_valider.grid(row=8, column=2)
        #ajouter un texte pour indiquer que les champs sont obligatoires
        label_obligatoire = Label(add_club, text="* : Champs obligatoires")
        label_obligatoire.grid(row=9, column=2)


    def supprimer_club(self):
        name = self.main_window_list.get(ANCHOR)
        nom = name.rsplit(' ',1)[0]
        print(nom)
        del_entry(self.conn, self.cursor, "CLUB", "NomClub", nom)
        update_tables(self.conn, self.cursor, "CLUB")

    def rafraichir(self):
        self.main_window.destroy()
        update_tables(self.conn, self.cursor, "CLUB")
        close_connection(self.conn)
        Clubs()


    def modifier_club(self):
        clubs = dict("CLUB")
        values = list(clubs.values())
        i = 0
        name = self.main_window_list.get(ANCHOR)
        nom = name.rsplit(' ',1)[0]
        print(nom)
        #on ouvre une fenetre
        modif_club = Tk()
        #on donne un titre a la fenetre
        modif_club.title("Modifier un club")
        #on donne une taille a la fenetre
        modif_club.geometry("400x200")
        #on crée un formulaire ou on affiche les données du club séléctionné
        if values[i][1] == "NOT NULL":
            text = "*"
        label_numero = Label(modif_club, text=f"Numéro de club : {text}")
        label_numero.grid(row=1, column=1)
        i+=1
        text = ""
        if values[i][1] == "NOT NULL":
            text = "*"
        label_nomclub = Label(modif_club, text=f"Nom du club : {text}")
        label_nomclub.grid(row=2, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_ville_club = Label(modif_club, text=f"Ville : {text}")
        label_ville_club.grid(row=3, column=1)
        i+=1
        text = ""
        if values[i][1] == "NOT NULL":
            text = "*"
        label_adresseclub = Label(modif_club, text=f"Adresse : {text}")
        label_adresseclub.grid(row=4, column=1)
        i+=1
        text = ""
        if values[i][1] == "NOT NULL":
            text = "*"
        label_cp_club = Label(modif_club, text=f"CP : {text}")
        label_cp_club.grid(row=5, column=1)
        i+=1
        text = ""
        if values[i][1] == "NOT NULL":
            text = "*"
        label_correspondant = Label(modif_club, text=f"Correspondant : {text}")
        label_correspondant.grid(row=6, column=1)
        i+=1
        text = ""
        if values[i][1] == "NOT NULL":
            text = "*"
        label_Tel = Label(modif_club, text=f"Téléphone : {text}")
        label_Tel.grid(row=7, column=1)
        text = ""
        #on recupere les données du club séléctionné

        data = getListRow(self.conn, self.cursor, "CLUB", ["NomClub"], [nom])
        #on les affiche dans le formulaire
        entry_numero_club = Entry(modif_club, width=30)
        entry_numero_club.grid(row=1, column=2)
        entry_numero_club.insert(END, data[0])
        entry_nom_club = Entry(modif_club, width=30)
        entry_nom_club.grid(row=2, column=2)
        entry_nom_club.insert(END, data[1])
        entry_ville_club = Entry(modif_club, width=30)
        entry_ville_club.grid(row=3, column=2)
        entry_ville_club.insert(END, data[2])
        entry_adresse_club = Entry(modif_club, width=30)
        entry_adresse_club.grid(row=4, column=2)
        entry_adresse_club.insert(END, data[3])
        entry_cp_club = Entry(modif_club, width=30)
        entry_cp_club.grid(row=5, column=2)
        entry_cp_club.insert(END, data[4])
        entry_correspondant_club = Entry(modif_club, width=30)
        entry_correspondant_club.grid(row=6, column=2)
        entry_correspondant_club.insert(END, data[5])
        entry_tel_club = Entry(modif_club, width=30)
        entry_tel_club.grid(row=7, column=2)
        entry_tel_club.insert(END, data[6])

        def modif_club_data():
            numero_club = entry_numero_club.get()
            nom_club = entry_nom_club.get()
            ville_club = entry_ville_club.get()
            adresse_club = entry_adresse_club.get()
            cp_club = entry_cp_club.get()
            correspondant_club = entry_correspondant_club.get()
            tel_club = entry_tel_club.get()
            # mettre les elements dans une liste
            a = [numero_club, nom_club, ville_club, adresse_club, cp_club, correspondant_club, tel_club]
            # print(a)
            checkInsertModify(self.conn, self.cursor, "CLUB", a, True, nom)
            
           

        #mettre les elements dans une liste
        #mod = [entry_numero_club, entry_nom_club, entry_ville_club, entry_adresse_club, entry_cp_club, entry_correspondant_club, entry_tel_club]
        #on crée un bouton pour valider les données
        button_valider = Button(modif_club, text="Valider", command = lambda : [modif_club_data(), modif_club.destroy()])
        button_valider.grid(row=8, column=2)
        label_obligatoire = Label(modif_club, text="* : Champs obligatoires")
        label_obligatoire.grid(row=9, column=2)

        #,X
       # button_valider = Button(add_club, text="Valider",command=lambda : [add_club_data(), update(liste_clubs)])
        #button_valider.grid(row=8, column=2)



    def retour(self):
        self.main_window.destroy()
        update_tables(self.conn, self.cursor, "CLUB")
        close_connection(self.conn)
        os.system("python Interface/main.py")

    def quitter(self):
        close_connection(self.conn)
        self.main_window.destroy()
    #afficher la fenetre
    # club.attributes('-fullscreen', True)