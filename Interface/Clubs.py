from tkinter import *
import os

def Clubs():
        #créer une fenetre
        club = Tk()
        #donner un titre a la club
        club.title("Clubs")
        #donner une taille a la club
        club.geometry("1920x1080")
        #creer une zone de texte pour les clubs
        zone_clubs = Text(club, height=1, width=75)
        zone_clubs.grid(row=3, column=2)
        #créer une liste de clubs et les afficher 
        liste_clubs = ["Club 1", "Club 2", "Club 3", "Club 4", "Club 5"]
        liste_clubs_afficher = Listbox(club, height=5, width=80)
        for i in range(len(liste_clubs)):
            liste_clubs_afficher.insert(i, liste_clubs[i])
        liste_clubs_afficher.grid(row=6, column=2)
    
        def retour():
            # bouton_retour.destroy()
            club.destroy()
            os.system("python Accueil.py")

        #creer bouton retour vers l'accueil
        bouton_retour = Button(club, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_retour.grid(row=18, column=2)

    
        #afficher la fenetre
        club.mainloop()

#afficher la fenetre
Clubs()
