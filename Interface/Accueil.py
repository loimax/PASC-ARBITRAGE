
from tkinter import *

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
            bouton_retour.destroy()
            club.destroy()
            Accueil()

        #creer bouton retour vers l'accueil
        bouton_retour = Button(club, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_retour.grid(row=18, column=2)

    
        #afficher la fenetre
        club.mainloop()

def Accueil():
        
        #creer une fenetre
        fenetre = Tk()

        #donner un titre a la fenetre
        fenetre.title("Arbitrage")

        #donner une taille a la fenetre
        fenetre.geometry("1920x1080")

        #mettre un logo a la fenetre
         fenetre.iconbitmap('Interface\img\logo2.ico')
        # logo = PhotoImage(file="img\logo2.png")
        # logo_label = Label(fenetre, image=logo)

        #couleur de fond de la fenetre
        fenetre.configure(background='#DADAD7')

        def tqt():
            bouton_clubs.destroy()
            bouton_Rencontres.destroy()
            bouton_JA.destroy()
            bouton_Affectation.destroy()
            bouton_Équipes.destroy()
            bouton_Quitter.destroy()
            fenetre.destroy()
            Clubs()
            #detruire les boutons
            
        
        def boom():
            fenetre.destroy()
            

        #creer 5 boutons
        bouton_clubs = Button(fenetre, text="Clubs", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=tqt)
        bouton_JA = Button(fenetre, text="JA", bg='#FF5733', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_Équipes = Button(fenetre, text="Équipes", bg='#FF5733', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_Rencontres = Button(fenetre, text="Rencontres", bg='#900C3F', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_Affectation = Button(fenetre, text="Affectation JA", bg='#900C3F', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_Quitter = Button(fenetre, text="Quitter" , command=boom, bg='#900C3F', fg='#000000', font=('Arial', 10, 'bold'))

        #placer les boutons dans la fenetre
        bouton_clubs.grid(row=3, column=2)
        bouton_JA.grid(row=6, column=2)
        bouton_Équipes.grid(row=9, column=2)
        bouton_Rencontres.grid(row=10, column=2)
        bouton_Affectation.grid(row=15, column=2)
        bouton_Quitter.grid(row=18, column=2)

        #taille des boutons
        bouton_clubs.config(height=5, width=80)
        bouton_JA.config(height=5, width=80)
        bouton_Équipes.config(height=5, width=80)
        bouton_Rencontres.config(height=5, width=80)
        bouton_Affectation.config(height=5, width=80)
        bouton_Quitter.config(height=5, width=80)

        #mettre un espace entre les boutons
        bouton_clubs.grid(padx=10, pady=10)
        bouton_JA.grid(padx=10, pady=10)
        bouton_Équipes.grid(padx=10, pady=10)
        bouton_Rencontres.grid(padx=10, pady=10)
        bouton_Affectation.grid(padx=10, pady=10)
        bouton_Quitter.grid(padx=10, pady=10)






        #afficher la fenetre
        fenetre.mainloop()

Accueil()

