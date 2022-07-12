from cmath import phase
from tkinter import *
import os
from tkinter.ttk import Combobox
from re import split
from datetime import date
from utils import *


class Equipes():
    def __init__(self):
        self.conn = create_connection("Interface/testdb/GestionRegionale.db")
        self.cursor = self.conn.cursor()
        if "Année" not in getAttributes(self.conn, self.cursor, "EquipeClub") and "Phase" not in getAttributes(self.conn, self.cursor, "EquipeClub"):
            alterTable(self.conn, self.cursor, "EquipeClub", [f"Année INTEGER NOT NULL DEFAULT {date.today().year}", "Phase INT NOT NULL DEFAULT 1"])
        if getMaxValue(self.conn, self.cursor, "EquipeClub", "Phase") == 1:
            switchPhaseDuplicates(self.conn, self.cursor, "EquipeClub")
        update_tables(self.conn, self.cursor, "EquipeClub", True)
        # créer une fenetre
        self.main_window = Tk()
        # donner un titre a la self.main_window
        self.main_window.title("Equipes")
        # donner une taille a la self.main_window
        self.main_window.geometry("1920x1080")
        self.main_window.attributes('-fullscreen', True)

        # créer 3 boutons pour les equipes : modifier ajouter supprimer
        title = Label(self.main_window, text="Liste des Equipes des Clubs :", font=('Arial', 24))
        
        bouton_modifier = Button(self.main_window, text="Modifier", fg='#000000', font=('Arial', 10, 'bold'),
                                      command=self.modifier_equipe)
        bouton_ajouter = Button(self.main_window, text="Ajouter", fg='#000000', font=('Arial', 10, 'bold'),
                                     command=self.add_equipe)
        bouton_supprimer = Button(self.main_window, text="Supprimer", fg='#000000', font=('Arial', 10, 'bold'),
                                       command=lambda: [self.supprimer_equipe()])
        bouton_rafraichir = Button(self.main_window, text="Rafraichir", fg='#000000', font=('Arial', 10, 'bold'),
                                        command=self.rafraichir)
        bouton_valider = Button(self.main_window, text="Valider", fg='#000000', font=('Arial', 10, 'bold'),command = self.valider)

        #créer une combobox avec un texte "Phase" au dessus
        self.entry2_phase = Entry(self.main_window, font=('Arial', 10, 'bold'), width=4)
        self.entry2_phase.place(x=0, y=0)
        #mettre le texte "Phase" 10 pixels à gauche de la combobox
        textphase = Label(self.main_window, text="Phase :", font=("Arial", 12))
        textphase.place(x=0, y=0)

        self.inputannee = Entry(self.main_window, font=("Arial", 12), width=7, justify=CENTER)
        self.inputannee.insert(0, date.today().year)
        self.inputannee.place(x=0, y=0)
        textannee = Label(self.main_window, text="Année :", font=("Arial", 12))
        textannee.place(x=0, y=0)
        

        # creer une zone de texte pour la recherche de equipes
        self.entry_equipe = Entry(self.main_window, font=("Arial", 20))
        self.entry_equipe.place(x=0, y=0)

        # créer une zone pour la liste de equipes
        self.team_list = Listbox(self.main_window, width=50)
        self.team_list.place(x = 0, y = 0)

        bouton_retour = Button(self.main_window, text="Retour", command=self.retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_quitter = Button(self.main_window, text="Quitter", command=self.quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        title.place(x = 0, y = 0)
        bouton_retour.place(x = 0, y = 0)
        bouton_quitter.place(x = 0, y = 0)
        bouton_valider.place(x = 0, y = 0)
        bouton_rafraichir.place(x = 0, y = 0)
        

        # # créer une liste de toutes les equipes en affichant UNIQUEMENT leur Rang
        # self.liste_equipes = creation_liste(self.conn, self.cursor, "EquipeClub", ["RangEq"])

        # self.liste_equipes = join_table(self.conn, self.cursor, ["CLUB", "EquipeClub"],
        #                                 ["CLUB.NumClub", "EquipeClub.numClub"], ["NomClub", "RangEq"])

        #final place
        self.main_window.update()


        title.place(x = self.main_window.winfo_width()/2 - title.winfo_width()/2, y = 50)
        bouton_valider.place(x=self.main_window.winfo_width()/2-bouton_valider.winfo_width()/2 + 220, y=125 )
        bouton_ajouter.place(x = self.main_window.winfo_width()/2 + self.entry_equipe.winfo_width()/2 + 50, y = 250 + ((self.team_list.winfo_height() - 3 * bouton_ajouter.winfo_height())/4))
        bouton_supprimer.place(x = self.main_window.winfo_width()/2 + self.entry_equipe.winfo_width()/2 + 50, y = 250 + (2 * (self.team_list.winfo_height() - 3 * bouton_ajouter.winfo_height())/4) + bouton_ajouter.winfo_height())
        bouton_modifier.place(x = self.main_window.winfo_width()/2 + self.entry_equipe.winfo_width()/2 + 50, y = 250 + (3 * (self.team_list.winfo_height() - 3 * bouton_ajouter.winfo_height())/4) + 2 * bouton_ajouter.winfo_height())
        bouton_rafraichir.place(x = self.main_window.winfo_width()/2 - bouton_rafraichir.winfo_width()/2, y = 450)
        bouton_retour.place(x = 0.02*self.main_window.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
        bouton_quitter.place(x = 0.98*self.main_window.winfo_width()-bouton_retour.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
        self.entry_equipe.place(x = self.main_window.winfo_width()/2 - self.entry_equipe.winfo_width()/2, y = 200)
        self.team_list.place(x = self.main_window.winfo_width()/2 - self.team_list.winfo_width()/2, y = 250)

        textannee.place(x = self.main_window.winfo_width()/2 - (textannee.winfo_width() + self.inputannee.winfo_width() + textphase.winfo_width() + self.entry2_phase.winfo_width() + 75)/2, y = 130)
        self.inputannee.place(x = self.main_window.winfo_width()/2 - (textannee.winfo_width() + self.inputannee.winfo_width() + textphase.winfo_width() + self.entry2_phase.winfo_width() + 75)/2 + textannee.winfo_width() + 25, y = 130)
        textphase.place(x = self.main_window.winfo_width()/2 - (textannee.winfo_width() + self.inputannee.winfo_width() + textphase.winfo_width() + self.entry2_phase.winfo_width() + 75)/2 + self.inputannee.winfo_width() + textannee.winfo_width() + 50, y = 130)
        self.entry2_phase.place(x = self.main_window.winfo_width()/2 - (textannee.winfo_width() + self.inputannee.winfo_width() + textphase.winfo_width() + self.entry2_phase.winfo_width() + 75)/2 + self.inputannee.winfo_width() + textannee.winfo_width() + textphase.winfo_width() + 75, y = 130)
        
        # Ajouter equipes dans la liste
        

        # afficher le equipe selectionné
        self.team_list.bind("<<ListboxSelect>>", self.fillout)

        # create a binding to the entry box
        self.entry_equipe.bind("<KeyRelease>", self.check)

        # afficher la fenetre
        
        self.main_window.mainloop()

    # uptade de la liste des equipes
    def update_listebox(self, data):
        # clear the listbox
        self.team_list.delete(0, END)

        # ajpouter les equipes dans la listbox
        for item in data:
            item_str = item[0] + " " + str(item[1]) + " " + item[2]
            self.team_list.insert(END, item_str)

    # afficher l'équipe sélectionnée
    def fillout(self, e):
        self.entry_equipe.delete(0, END)
        self.entry_equipe.insert(0, self.team_list.get(ANCHOR))

    # créer fonction entrée vs liste d'équipes
    def check(self, e):
        # grab what typed
        typed = self.entry_equipe.get()
        # print("self.liste_equipes", self.liste_equipes)

        if typed == '':
            data = self.liste_equipes
        else:
            data = []
            for item in self.liste_equipes:
                item_str = item[0] + " " + str(item[1]) + " " + item[2]
                if typed.lower() in item_str.lower():
                    data.append(item)

        self.update_listebox(data)

    # faire une fonction qui ouvre un formulaire pour ajouter une équipe lorsqu'on clique sur le bouton
    def add_equipe(self):
        clubs = dict("EquipeClub")
        values = list(clubs.values())
        i = 1
        # récupère les données de l'équipe sélectionné
        chaine_clubXekip = self.team_list.get(ANCHOR)
        nom_club = chaine_clubXekip[:-5]
        num_club = getValues(self.conn, self.cursor, "CLUB", "NumClub", "NomClub", [nom_club])
        # créer une fenetre
        add_equipe = Tk()
        # donner un titre a la fenetre
        add_equipe.title("Ajouter une équipe")
        # donner une taille a la fenetre
        add_equipe.geometry("400x270")
        # couleur de fond de la fenetre
        add_equipe.configure(background='#DADAD7')
        # créer une zone de texte pour le numéro de l'équipe
        # entry_numero_equipe = Entry(add_equipe, width=30)
        # entry_numero_equipe.grid(row=1, column=2)
        # créer une zone de texte pour le numéro du club
        entry_numero_club = Entry(add_equipe, width=30)
        entry_numero_club.grid(row=2, column=2)
        entry_numero_club.insert(0, num_club)
        # créer une zone de texte pour le rang de l'équipe
        entry_rang_equipe = Entry(add_equipe, width=30)
        entry_rang_equipe.grid(row=3, column=2)
        # créer une zone de texte pour savoir si c'est une équipe masculine ou non
        entry_masculin = Entry(add_equipe, width=30)
        entry_masculin.grid(row=4, column=2)
        # créer une zone de texte pour la division de l'équipe
        entry_division = Entry(add_equipe, width=30)
        entry_division.grid(row=5, column=2)
        # créer une zone de texte pour le nom de la poule
        entry_poule = Entry(add_equipe, width=30)
        entry_poule.grid(row=6, column=2)
        # créer une zone de texte pour le correq
        entry_correq = Entry(add_equipe, width=30)
        entry_correq.grid(row=7, column=2)
        # créer une zone de texte pour les noms des années
        entry_annee = Entry(add_equipe, width=30)
        entry_annee.grid(row=8, column=2)
        # créer une zone de texte pour les noms des phases
        entry_phase = Entry(add_equipe, width=30)
        entry_phase.grid(row=9, column=2)

        # afficher les titres des zones de texte

        # if values[i][1] == "NOT NULL":
        #     text = "*"
        # label_numero = Label(add_equipe, text=f"Numéro d'équipe : {text}")
        # label_numero.grid(row=1, column=1)
        # i+=1
        # text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_numero_club = Label(add_equipe, text=f"Numéro du club : {text}")
        label_numero_club.grid(row=2, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_rang_equipe = Label(add_equipe, text=f"Rang équipe : {text}")
        label_rang_equipe.grid(row=3, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_masculin = Label(add_equipe, text=f"Masculin : {text}")
        label_masculin.grid(row=4, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_division = Label(add_equipe, text=f"Division : {text}")
        label_division.grid(row=5, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_poule = Label(add_equipe, text=f"Poule : {text}")
        label_poule.grid(row=6, column=1)
        i+=1
        text = ""
        
        if values[i][1] == "NOT NULL":
            text = "*"
        label_correq = Label(add_equipe, text=f"CorrEq : {text}")
        label_correq.grid(row=7, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_annee = Label(add_equipe, text=f"Année : {text}")
        label_annee.grid(row=8, column=1)
        i+=1
        text = ""

        if values[i][1] == "NOT NULL":
            text = "*"
        label_phase = Label(add_equipe, text=f"Numéro de phase : {text}")
        label_phase.grid(row=9, column=1)
        i+=1
        text = ""
        

        # recuperer les données du formulaire
        def add_equipe_data():
            # numero_equipe = entry_numero_equipe.get()
            numero_club = entry_numero_club.get()
            rang_equipe = entry_rang_equipe.get()
            masculin = entry_masculin.get()
            division = entry_division.get()
            poule = entry_poule.get()
            annee = entry_annee.get()
            phase = entry_phase.get()
            # mettre les elements dans une liste
            # print(numero_equipe, numero_club, rang_equipe, masculin, division, poule, annee, phase)
            data = [numero_club, rang_equipe, masculin, division, poule, "None", annee, phase]
            
            checkInsertModify(self.conn, self.cursor, "EquipeClub", data)
            add_equipe.destroy()

        # créer un bouton pour valider les données
        button_valider = Button(add_equipe, text="Valider", command=lambda: [add_equipe_data()])
        button_valider.grid(row=10, column=2)
        #ajouter un texte pour indiquer que les champs sont obligatoires
        label_obligatoire = Label(add_equipe, text="* : Champs obligatoires")
        label_obligatoire.grid(row=11, column=2)
        

    def supprimer_equipe(self):
        chaine_clubXekip = self.team_list.get(ANCHOR)
        chaine_split = split(' ', chaine_clubXekip)
        division_equipe = chaine_split[len(chaine_split) - 1]
        nom_club = str(chaine_clubXekip[:-5])
        num_club = getValues(self.conn, self.cursor, "CLUB", "NumCLUB", "NomClub", [nom_club])[0]
        num_equipe = getValuesConstraints(self.conn, self.cursor, "EquipeClub", "numEq", ["numClub", "Division"], [num_club, division_equipe])[0]
        del_entry(self.conn, self.cursor, "EquipeClub", "numEq", num_equipe)
        update_tables(self.conn, self.cursor, "EquipeClub")

    def rafraichir(self):
        self.main_window.destroy()
        update_tables(self.conn, self.cursor, "EquipeClub")
        close_connection(self.conn)
        Equipes()

    def valider(self):
        phase = self.entry2_phase.get()
        annee = self.inputannee.get()
        # print(phase)
        self.liste_equipes = join_table_where(self.conn, self.cursor, ["CLUB", "EquipeClub"], ["CLUB.NumClub", "EquipeClub.numClub"], \
            ["NomClub", "RangEq", "Division"], ["Phase", "Année"], [phase, annee])
        self.update_listebox(self.liste_equipes)

        

    def modifier_equipe(self):
        clubs = dict("EquipeClub")
        values = list(clubs.values())
        # récupère la chaine dans la boite de dialogue
        chaine_clubXekip = self.team_list.get(ANCHOR)
        # récupère chaque élément de la chaine lue dans des variables séparées
        nom_club = str(chaine_clubXekip[:-5])

        chaine_split = split(' ', chaine_clubXekip)
        rang_equipe = chaine_split[len(chaine_split)-2]
        division_equipe = chaine_split[len(chaine_split)-1]
        num_club = getValues(self.conn, self.cursor, "CLUB", "NumCLUB", "NomClub", [nom_club])[0]
        phase = self.entry2_phase.get()
        num_equipe = getValuesConstraints(self.conn, self.cursor, "EquipeClub", "numEq", ["numClub", "RangEq", "Phase"],
                                          [num_club, rang_equipe, phase])[0]
        # print("nom_club = ", nom_club, "num_club = ", num_club, "rang_equipe = ", rang_equipe, "division = ", division_equipe, "phase = ", phase, "num equipe = ", num_equipe)

        # on ouvre une fenetre
        modif_equipe = Tk()
        # on donne un titre a la fenetre
        modif_equipe.title("Modifier une équipe")
        # on donne une taille a la fenetre
        modif_equipe.geometry("400x270")

        query = f"SELECT * FROM EquipeClub WHERE numEq = {num_equipe}"
        cur = execute_query(self.conn, self.cursor, query)
        data = cur.fetchall()[0]

        # # on crée un formulaire ou on affiche les données du equipe séléctionné
        # if values[i][1] == "NOT NULL":
        #     text = "*"
        # label_numero = Label(modif_equipe, text=f"Numéro d'équipe : {text}")
        # label_numero.grid(row=1, column=1)
        # entry_numero_equipe = Entry(modif_equipe, width=30)
        # entry_numero_equipe.grid(row=i+1, column=2)
        # entry_numero_equipe.insert(END, data[0])
        # i+=1
        text = "*"
        i = 0
        label_numero_club = Label(modif_equipe, text=f"Numéro du club : {text}")
        label_numero_club.grid(row=i+1, column=1)
        entry_numero_club = Entry(modif_equipe, width=30)
        entry_numero_club.grid(row=i+1, column=2)
        entry_numero_club.insert(END, data[1])
        i+=1

        
        label_rang_equipe = Label(modif_equipe, text=f"Rang équipe : {text}")
        label_rang_equipe.grid(row=i+1, column=1)
        entry_rang_equipe = Entry(modif_equipe, width=30)
        entry_rang_equipe.grid(row=i+1, column=2)
        entry_rang_equipe.insert(END, data[2])
        i+=1

        
        label_masculin = Label(modif_equipe, text=f"Masculin : {text}")
        label_masculin.grid(row=i+1, column=1)
        entry_masculin = Entry(modif_equipe, width=30)
        entry_masculin.grid(row=i+1, column=2)
        entry_masculin.insert(END, data[3])
        i+=1

        
        label_division = Label(modif_equipe, text=f"Division : {text}")
        label_division.grid(row=i+1, column=1)
        entry_division = Entry(modif_equipe, width=30)
        entry_division.grid(row=i+1, column=2)
        entry_division.insert(END, data[4])
        i+=1

        
        label_poule = Label(modif_equipe, text=f"Poule : {text}")
        label_poule.grid(row=i+1, column=1)
        entry_poule = Entry(modif_equipe, width=30)
        entry_poule.grid(row=i+1, column=2)
        entry_poule.insert(END, data[5])
        i+=1
        
        
        text = ""
        label_correq = Label(modif_equipe, text=f"CorrEq : {text}")
        label_correq.grid(row=i+1, column=1)
        entry_correq = Entry(modif_equipe, width=30)
        entry_correq.grid(row=i+1, column=2)
        entry_correq.insert(END, data[6])
        i+=1
        text = "*"

        
        label_annee = Label(modif_equipe, text=f"Année : {text}")
        label_annee.grid(row=i+1, column=1)
        entry_annee = Entry(modif_equipe, width=30)
        entry_annee.grid(row=i+1, column=2)
        entry_annee.insert(END, data[7])
        i+=1

        
        label_phase = Label(modif_equipe, text=f"Numéro de phase : {text}")
        label_phase.grid(row=i+1, column=1)
        entry_phase = Entry(modif_equipe, width=30)
        entry_phase.grid(row=i+1, column=2)
        entry_phase.insert(END, data[8])
        i+=1

        def modif_equipe_data():
            numero_equipe = data[0]
            numero_club = entry_numero_club.get()
            rang_equipe = entry_rang_equipe.get()
            masculin = entry_masculin.get()
            division = entry_division.get()
            poule = entry_poule.get()
            correq = entry_correq.get()
            annee = entry_annee.get()
            phase = entry_phase.get()
            # mettre les elements dans une liste
            a = [numero_equipe, numero_club, rang_equipe, masculin, division, poule, correq, annee, phase]
            # modify_entry(self.conn, self.cursor, "EquipeClub", a, getID(data))
            checkInsertModify(self.conn, self.cursor, "EquipeClub", a, True, num_equipe)

        # mettre les elements dans une liste
        # mod = [entry_numero_equipe, entry_numero_club, entry_ville_equipe, entry_rang_equipe, entry_masculin, entry_division, entry_poule]
        # on crée un bouton pour valider les données
        button_valider = Button(modif_equipe, text="Valider", command = lambda : [modif_equipe_data(), modif_equipe.destroy()])
        button_valider.grid(row=10, column=2)
        label_obligatoire = Label(modif_equipe, text="* : Champs obligatoires")
        label_obligatoire.grid(row=11, column=2)
        
        # ,X
        #ajouter un texte pour indiquer que les champs sont obligatoires

        

    # button_valider = Button(add_equipe, text="Valider",command=lambda : [add_self.main_window_data(), update_listebox(liste_equipes)])
    # button_valider.grid(row=8, column=2)

    def retour(self):
        self.main_window.destroy()
        update_tables(self.conn, self.cursor, "EquipeClub")
        close_connection(self.conn)
        os.system("python Interface/main.py")

    def quitter(self):
        update_tables(self.conn, self.cursor, "EquipeClub")
        close_connection(self.conn)
        self.main_window.destroy()