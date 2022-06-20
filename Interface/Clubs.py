from tkinter import *
import os

import sys

from testdb.ex import display_nom_club




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

        #créer 3 boutons pour les clubs : modifier ajouter supprimer
        bouton_modifier = Button(club, text="Modifier", fg='#000000', font=('Arial', 10, 'bold'))
        bouton_modifier.place(x=600, y=400)
        bouton_ajouter = Button(club, text="Ajouter", fg='#000000', font=('Arial', 10, 'bold'))
        bouton_ajouter.place(x=725, y=400)
        bouton_supprimer = Button(club, text="Supprimer", fg='#000000', font=('Arial', 10, 'bold'))
        bouton_supprimer.place(x=850, y=400)

        #creer une zone de texte pour la recherche de clubs
        entry_clubs = Entry(club, font=("Helvetica", 20))
        entry_clubs.place(x=600, y=150)

        #créer une zone pour la liste de clubs
        club_list = Listbox(club, width=50)
        club_list.place(x=600, y=200)

        #créer une liste de clubs 
        liste_clubs = display_nom_club()

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