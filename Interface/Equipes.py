from tkinter import *
import os

import sys
from tkinter.ttk import Combobox

from utils import *


def Equipes():
    # créer une fenetre
    main_window = Tk()
    # donner un titre a la main_window
    main_window.title("Equipes")
    # donner une taille a la main_window
    main_window.geometry("1920x1080")

    # uptade de la liste des equipes
    def update(data):
        print("update")
        # clear the listbox
        club_list.delete(0, END)

        # ajpouter les equipes dans la listbox
        for item in data:
            club_list.insert(END, item)

    # afficher le equipe séléctionné
    def fillout(e):
        entry_club.delete(0, END)
        entry_club.insert(0, club_list.get(ANCHOR))
        equipe_liste = getListRow("EquipeClub", ["numClub"], []) #AFAIRE

    # créer fonction entrée vs liste de equipes
    def check(e):
        # grab what typed
        typed = entry_club.get()

        if typed == '':
            data = liste_equipes
        else:
            data = []
            for item in liste_equipes:
                if typed.lower() in item.lower():
                    data.append(item)

        update(data)

    # faire une fonction qui ouvre un formulaire pour ajouter un equipe lorque on clique sur le bouton
    def add_equipe():
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
            insert_entry("EquipeClub", data)
            add_equipe.destroy()

        # créer un bouton pour valider les données
        button_valider = Button(add_equipe, text="Valider", command=lambda: [add_equipe_data()])
        button_valider.grid(row=8, column=2)


    def supprimer_equipe():
        num = equipe_list.get(ANCHOR)
        del_entry("EquipeClub", "numEq", num)


    def rafraichir():
        main_window.destroy()
        os.system("python Interface\Equipes.py")


    def modifier_equipe():
        num = equipe_list.get(ANCHOR)
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
        data = getListRow("EquipeClub", ["RangEq"], [num])
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
            modify_entry("EquipeClub", a, getID(data))
            print(getListRow("EquipeClub", ["numEq"], [num]))
            print(display_table("EquipeClub"))

        # mettre les elements dans une liste
        # mod = [entry_numero_equipe, entry_numero_club, entry_ville_equipe, entry_rang_equipe, entry_masculin, entry_division, entry_poule]
        # on crée un bouton pour valider les données
        button_valider = Button(modif_equipe, text="Valider", command=modif_equipe_data)
        button_valider.grid(row=8, column=2)
        # ,X

    # button_valider = Button(add_equipe, text="Valider",command=lambda : [add_main_window_data(), update(liste_equipes)])
    # button_valider.grid(row=8, column=2)

    # créer 3 boutons pour les equipes : modifier ajouter supprimer
    bouton_modifier = Button(main_window, text="Modifier", fg='#000000', font=('Arial', 10, 'bold'), command=modifier_equipe)
    bouton_modifier.place(x=600, y=400)
    bouton_ajouter = Button(main_window, text="Ajouter", fg='#000000', font=('Arial', 10, 'bold'), command=add_equipe)
    bouton_ajouter.place(x=725, y=400)
    bouton_supprimer = Button(main_window, text="Supprimer", fg='#000000', font=('Arial', 10, 'bold'),
                              command=lambda: [supprimer_equipe()])
    bouton_supprimer.place(x=850, y=400)
    bouton_rafraichir = Button(main_window, text="Rafraichir", fg='#000000', font=('Arial', 10, 'bold'),
                               command=rafraichir)
    bouton_rafraichir.place(x=720, y=500)

    # Menu déroulant équipe
    equipe_liste = []
    menu_deroulant_equipes = Combobox(equipe, values=equipe_liste, font=("Arial", 12))

    # creer une zone de texte pour la recherche de equipes
    entry_club = Entry(main_window, font=("Helvetica", 20))
    entry_club.place(x=600, y=150)

    menu_deroulant_equipes.place(x=1000, y=150, width=120)

    # créer une zone pour la liste de equipes
    club_list = Listbox(main_window, width=50)
    club_list.place(x=600, y=200)


    # créer une liste de equipes
    liste_club = creation_liste("CLUB", "NomClub")

    # Ajouter equipes dans la liste
    update(liste_club)

    # afficher le equipe selectionné
    club_list.bind("<<ListboxSelect>>", fillout)

    # create a binding to the entry box
    entry_club.bind("<KeyRelease>", check)

    def retour():
        # bouton_retour.destroy()
        main_window.destroy()
        os.system("python Interface\Accueil.py")

    # creer bouton retour vers l'accueil
    bouton_retour = Button(main_window, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
    bouton_retour.place(x=725, y=700)

    # afficher la fenetre
    main_window.mainloop()


# afficher la fenetre
Equipes()