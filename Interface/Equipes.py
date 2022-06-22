from tkinter import *
import os
import sys
from tkinter.ttk import Combobox

from utils import *


class Equipes():
    def __init__(self):
        self.conn = create_connection("Interface/testdb/GestionRegionale.db")
        self.cursor = self.conn.cursor()

        # créer une fenetre
        self.main_window = Tk()
        # donner un titre a la self.main_window
        self.main_window.title("Equipes")
        # donner une taille a la self.main_window
        self.main_window.geometry("1920x1080")

        # créer 3 boutons pour les equipes : modifier ajouter supprimer
        self.bouton_modifier = Button(self.main_window, text="Modifier", fg='#000000', font=('Arial', 10, 'bold'),
                                 command=self.modifier_equipe)
        self.bouton_modifier.place(x=600, y=400)
        self.bouton_ajouter = Button(self.main_window, text="Ajouter", fg='#000000', font=('Arial', 10, 'bold'),
                                command=self.add_equipe)
        self.bouton_ajouter.place(x=725, y=400)
        self.bouton_supprimer = Button(self.main_window, text="Supprimer", fg='#000000', font=('Arial', 10, 'bold'),
                                  command=lambda: [self.supprimer_equipe()])
        self.bouton_supprimer.place(x=850, y=400)
        self.bouton_rafraichir = Button(self.main_window, text="Rafraichir", fg='#000000', font=('Arial', 10, 'bold'),
                                   command=self.rafraichir)
        self.bouton_rafraichir.place(x=720, y=500)

        # creer une zone de texte pour la recherche de equipes
        self.entry_equipe = Entry(self.main_window, font=("Helvetica", 20))
        self.entry_equipe.place(x=600, y=150)

        # créer une zone pour la liste de equipes
        self.team_list = Listbox(self.main_window, width=50)
        self.team_list.place(x=600, y=200)

        # créer une liste de equipes
        self.liste_equipes = creation_liste(self.conn, self.cursor, "EquipeClub", ["RangEq"])

        # Ajouter equipes dans la liste
        self.update_listebox(self.liste_equipes)

        # afficher le equipe selectionné
        self.team_list.bind("<<ListboxSelect>>", self.fillout)

        # create a binding to the entry box
        self.entry_equipe.bind("<KeyRelease>", self.check)

        # creer bouton retour vers l'accueil
        bouton_retour = Button(self.main_window, text="Retour", command=self.retour, bg='#AF7AC5', fg='#000000',
                               font=('Arial', 10, 'bold'))
        bouton_retour.place(x=725, y=700)

        # afficher la fenetre
        self.main_window.mainloop()

    # uptade de la liste des equipes
    def update_listebox(self, data):
        # clear the listbox
        self.team_list.delete(0, END)

        # ajpouter les equipes dans la listbox
        for item in data:
            self.team_list.insert(END, item)

    # afficher l'equipe séléctionné
    def fillout(self, e):
        self.entry_equipe.delete(0, END)
        self.entry_equipe.insert(0, self.team_list.get(ANCHOR))
        # team_liste = getListRow(self.conn, self.cursor, "EquipeClub", ["numClub"], []) #AFAIRE

    # créer fonction entrée vs liste de equipes
    def check(self, e):
        # grab what typed
        typed = self.entry_equipe.get()

        if typed == '':
            data = self.liste_equipes
        else:
            data = []
            for item in self.liste_equipes:
                if typed.lower() in item.lower():
                    data.append(item)

        self.update_listebox(data)

    # faire une fonction qui ouvre un formulaire pour ajouter un equipe lorque on clique sur le bouton
    def add_equipe(self):
        # créer une fenetre
        add_equipe = Tk()
        # donner un titre a la fenetre
        add_equipe.title("Ajouter une équipe")
        # donner une taille a la fenetre
        add_equipe.geometry("400x200")
        # couleur de fond de la fenetre
        add_equipe.configure(background='#DADAD7')
        # créer une zone de texte pour les noms des equipes
        entry_numero_equipe = Entry(add_equipe, width=30)
        entry_numero_equipe.grid(row=1, column=2)
        # créer une zone de texte pour les noms des equipes
        entry_numero_club = Entry(add_equipe, width=30)
        entry_numero_club.grid(row=2, column=2)
        # créer une zone de texte pour les noms des equipes
        entry_rang_equipe = Entry(add_equipe, width=30)
        entry_rang_equipe.grid(row=3, column=2)
        # créer une zone de texte pour les noms des equipes
        entry_masculin = Entry(add_equipe, width=30)
        entry_masculin.grid(row=4, column=2)
        # créer une zone de texte pour les noms des equipes
        entry_division = Entry(add_equipe, width=30)
        entry_division.grid(row=5, column=2)
        # créer une zone de texte pour les noms des equipes
        entry_poule = Entry(add_equipe, width=30)
        entry_poule.grid(row=6, column=2)
        # afficher les titres des zones de texte
        label_numero = Label(add_equipe, text="Numéro d'équipe :")
        label_numero.grid(row=1, column=1)
        label_numero_club = Label(add_equipe, text="Numéro du club :")
        label_numero_club.grid(row=2, column=1)
        label_rang_equipe = Label(add_equipe, text="Rang équipe :")
        label_rang_equipe.grid(row=3, column=1)
        label_masculin = Label(add_equipe, text="Masculin :")
        label_masculin.grid(row=4, column=1)
        label_division = Label(add_equipe, text="Division :")
        label_division.grid(row=5, column=1)
        label_poule = Label(add_equipe, text="Poule :")
        label_poule.grid(row=6, column=1)

        # recuperer les données du formulaire
        def add_equipe_data():
            numero_equipe = entry_numero_equipe.get()
            numero_club = entry_numero_club.get()
            rang_equipe = entry_rang_equipe.get()
            masculin = entry_masculin.get()
            division = entry_division.get()
            poule = entry_poule.get()
            # mettre les elements dans une liste
            print(numero_equipe, numero_club, rang_equipe, masculin, division, poule)
            data = [numero_equipe, numero_club, rang_equipe, masculin, division, poule, "None"]
            insert_entry(self.conn, self.cursor, "EquipeClub", data)
            add_equipe.destroy()

        # créer un bouton pour valider les données
        button_valider = Button(add_equipe, text="Valider", command=lambda: [add_equipe_data()])
        button_valider.grid(row=8, column=2)


    def supprimer_equipe(self):
        num = self.team_list.get(ANCHOR)
        del_entry(self.conn, self.cursor, "EquipeClub", "numEq", num)


    def rafraichir(self):
        self.main_window.destroy()
        Equipes()
        # os.system("python Interface\Equipes.py")


    def modifier_equipe(self):
        num = self.team_list.get(ANCHOR)
        # on ouvre une fenetre
        modif_equipe = Tk()
        # on donne un titre a la fenetre
        modif_equipe.title("Modifier une équipe")
        # on donne une taille a la fenetre
        modif_equipe.geometry("400x200")
        # on crée un formulaire ou on affiche les données du equipe séléctionné
        label_numero = Label(modif_equipe, text="Numéro d'équipe :")
        label_numero.grid(row=1, column=1)
        label_num_club = Label(modif_equipe, text="Numéro du club :")
        label_num_club.grid(row=2, column=1)
        label_rang_eq = Label(modif_equipe, text="Rang de l'équipe :")
        label_rang_eq.grid(row=3, column=1)
        label_masculin = Label(modif_equipe, text="Masculin :")
        label_masculin.grid(row=4, column=1)
        label_division = Label(modif_equipe, text="Division :")
        label_division.grid(row=5, column=1)
        label_poule = Label(modif_equipe, text="Poule :")
        label_poule.grid(row=6, column=1)
        # on recupere les données de l'equipe séléctionné
        data = getListRow(self.conn, self.cursor, "EquipeClub", ["RangEq"], [num])
        # on les affiche dans le formulaire
        entry_numero_equipe = Entry(modif_equipe, width=30)
        entry_numero_equipe.grid(row=1, column=2)
        entry_numero_equipe.insert(END, data[0])
        entry_numero_club = Entry(modif_equipe, width=30)
        entry_numero_club.grid(row=2, column=2)
        entry_numero_club.insert(END, data[1])
        entry_rang_equipe = Entry(modif_equipe, width=30)
        entry_rang_equipe.grid(row=3, column=2)
        entry_rang_equipe.insert(END, data[2])
        entry_masculin = Entry(modif_equipe, width=30)
        entry_masculin.grid(row=4, column=2)
        entry_masculin.insert(END, data[3])
        entry_division = Entry(modif_equipe, width=30)
        entry_division.grid(row=5, column=2)
        entry_division.insert(END, data[4])
        entry_poule = Entry(modif_equipe, width=30)
        entry_poule.grid(row=6, column=2)
        entry_poule.insert(END, data[5])

        def modif_equipe_data():
            numero_equipe = entry_numero_equipe.get()
            numero_club = entry_numero_club.get()
            rang_equipe = entry_rang_equipe.get()
            masculin = entry_masculin.get()
            division = entry_division.get()
            poule = entry_poule.get()
            # mettre les elements dans une liste
            a = [numero_equipe, numero_club, rang_equipe, masculin, division, poule]
            modify_entry(self.conn, self.cursor, "EquipeClub", a, getID(data))
            print(getListRow(self.conn, self.cursor, "EquipeClub", ["numEq"], [num]))
            print(display_table(self.conn, self.cursor, "EquipeClub"))

        # mettre les elements dans une liste
        # mod = [entry_numero_equipe, entry_numero_club, entry_ville_equipe, entry_rang_equipe, entry_masculin, entry_division, entry_poule]
        # on crée un bouton pour valider les données
        button_valider = Button(modif_equipe, text="Valider", command=modif_equipe_data)
        button_valider.grid(row=8, column=2)
        # ,X

    # button_valider = Button(add_equipe, text="Valider",command=lambda : [add_self.main_window_data(), update_listebox(liste_equipes)])
    # button_valider.grid(row=8, column=2)

    def retour(self):
        # bouton_retour.destroy()
        self.main_window.destroy()
        os.system("python Interface/main.py")
