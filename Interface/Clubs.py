from tkinter import *
import os

import sys

from utils import *




def Clubs():
        #créer une fenetre
        club = Tk()
        #donner un titre a la club
        club.title("Clubs")
        #donner une taille a la club
        club.geometry("1920x1080")

        #uptade de la liste des clubs
        def update(data):
            #clear the listbox
            club_list.delete(0, END)

            #ajpouter les clubs dans la listbox
            for item in data:
                club_list.insert(END, item)
        #afficher le club séléctionné
        def fillout(e):
            entry_clubs.delete(0, END)
            entry_clubs.insert(0, club_list.get(ANCHOR))

        #créer fonction entrée vs liste de clubs
        def check(e):
            #grab what typed
            typed = entry_clubs.get()

            if typed == '':
                data = liste_clubs
            else:
                data = []
                for item in liste_clubs:
                    if typed.lower() in item.lower():
                        data.append(item)

            update(data)
        
        #faire une fonction qui ouvre un formulaire pour ajouter un club lorque on clique sur le bouton
        def add_club():
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
            label_numero = Label(add_club, text="Numéro de club :")
            label_numero.grid(row=1, column=1)
            label_nomclub = Label(add_club, text="Nom du club :")
            label_nomclub.grid(row=2, column=1)
            label_ville_club = Label(add_club, text="Ville :")
            label_ville_club.grid(row=3, column=1)
            label_adresseclub = Label(add_club, text="Adresse :")
            label_adresseclub.grid(row=4, column=1)
            label_cp_club = Label(add_club, text="CP :")
            label_cp_club.grid(row=5, column=1)
            label_correspondant = Label(add_club, text="Correspondant :")
            label_correspondant.grid(row=6, column=1)
            label_Tel = Label(add_club, text="Téléphone :")
            label_Tel.grid(row=7, column=1)
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
                insert_entry("CLUB", data)
                
        
                
            #créer un bouton pour valider les données
            button_valider = Button(add_club, text="Valider",command=add_club_data)
            button_valider.grid(row=8, column=2)
            

            


        def supprimer_club():
            print("supprimer club")
            


        #créer 3 boutons pour les clubs : modifier ajouter supprimer
        bouton_modifier = Button(club, text="Modifier", fg='#000000', font=('Arial', 10, 'bold'))
        bouton_modifier.place(x=600, y=400)
        bouton_ajouter = Button(club, text="Ajouter", fg='#000000', font=('Arial', 10, 'bold'),command=add_club)
        bouton_ajouter.place(x=725, y=400)
        bouton_supprimer = Button(club, text="Supprimer", fg='#000000', font=('Arial', 10, 'bold'), command=supprimer_club)
        bouton_supprimer.place(x=850, y=400)

        #creer une zone de texte pour la recherche de clubs
        entry_clubs = Entry(club, font=("Helvetica", 20))
        entry_clubs.place(x=600, y=150)

        #créer une zone pour la liste de clubs
        club_list = Listbox(club, width=50)
        club_list.place(x=600, y=200)

        #créer une liste de clubs 
        liste_clubs = creation_liste("CLUB", "NomClub")

        #Ajouter clubs dans la liste
        update(liste_clubs)

        #afficher le club selectionné
        club_list.bind("<<ListboxSelect>>", fillout)

        #create a binding to the entry box
        entry_clubs.bind("<KeyRelease>", check)


       


        # def ajouter():
        #     liste_clubs.append(zone_clubs.get("1.0", END))
        #     liste_clubs_afficher.insert(END, zone_clubs.get("1.0", END))
        #     zone_clubs.delete("1.0", END)
        #     print(liste_clubs)
        

         #creer 3 boutons pour les JA : modifier ajouter supprimer
        # creer bouton modifier
       # bouton_modifier = Button(club, text="Modifier", bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        #bouton_modifier.grid(row=8, column=2)
        # creer bouton ajouter
       # bouton_ajouter = Button(club, text="Ajouter", bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'),command=ajouter)
      #  bouton_ajouter.grid(row=9, column=2)
        # creer bouton supprimer
       # bouton_supprimer = Button(club, text="Supprimer", bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
      #  bouton_supprimer.grid(row=10, column=2)
        #placer les boutons dans la fenetre
        # bouton_modifier.place(x=700, y=10)
        # bouton_ajouter.place(x=700, y=50)
        # bouton_supprimer.place(x=700, y=90)
    
        def retour():
            # bouton_retour.destroy()
            club.destroy()
            os.system("python Interface\Accueil.py")

        #creer bouton retour vers l'accueil
        bouton_retour = Button(club, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_retour.place(x=725, y=700)

    
        #afficher la fenetre
        club.mainloop()

#afficher la fenetre
Clubs()