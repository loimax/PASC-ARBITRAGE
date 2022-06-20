from tkinter import *
import os

def Rencontre():
        #créer une fenetre
        Rencontre = Tk()
        #donner un titre a la Rencontre
        Rencontre.title("Rencontres")
        #donner une taille a la Rencontre
        Rencontre.geometry("1920x1080")
        #creer une zone de texte pour les Rencontres
        zone_Rencontres = Text(Rencontre, height=1, width=75)
        zone_Rencontres.grid(row=3, column=2)
        #créer une liste de Rencontres et les afficher 
        liste_Rencontres = ["Rencontre 1", "Rencontre 2", "Rencontre 3", "Rencontre 4", "Rencontre 5"]
        liste_Rencontres_afficher = Listbox(Rencontre, height=5, width=80)
        for i in range(len(liste_Rencontres)):
            liste_Rencontres_afficher.insert(i, liste_Rencontres[i])
        liste_Rencontres_afficher.grid(row=6, column=2)
    
        def retour():
            # bouton_retour.destroy()
            Rencontre.destroy()
            os.system("python Interface/Accueil.py")

        #creer bouton retour vers l'accueil
        bouton_retour = Button(Rencontre, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_retour.grid(row=18, column=2)

    
        #afficher la fenetre
        Rencontre.mainloop()

#afficher la fenetre
Rencontre()