from tkinter import *
import os

def JA():
        #créer une fenetre
        JA = Tk()
        #donner un titre a la JA
        JA.title("JAs")
        #donner une taille a la JA
        JA.geometry("1920x1080")
        #creer une zone de texte pour les JAs
        zone_JAs = Text(JA, height=1, width=75)
        zone_JAs.grid(row=3, column=2)
        #créer une liste de JAs et les afficher 
        liste_JAs = ["JA 1", "JA 2", "JA 3", "JA 4", "JA 5"]
        liste_JAs_afficher = Listbox(JA, height=5, width=80)
        for i in range(len(liste_JAs)):
            liste_JAs_afficher.insert(i, liste_JAs[i])
        liste_JAs_afficher.grid(row=6, column=2)
    
        def retour():
            # bouton_retour.destroy()
            JA.destroy()
            os.system("python Interface/Accueil.py")

        #creer bouton retour vers l'accueil
        bouton_retour = Button(JA, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_retour.grid(row=18, column=2)

    
        #afficher la fenetre
        JA.mainloop()

#afficher la fenetre
JA()
