
from tkinter import *
import os 
# def Clubs():
#         #créer une fenetre
#         club = Tk()
#         #donner un titre a la club
#         club.title("Clubs")
#         #donner une taille a la club
#         club.geometry("1920x1080")
#         #creer une zone de texte pour les clubs
#         zone_clubs = Text(club, height=1, width=75)
#         zone_clubs.grid(row=3, column=2)
#         #créer une liste de clubs et les afficher 
#         liste_clubs = ["Club 1", "Club 2", "Club 3", "Club 4", "Club 5"]
#         liste_clubs_afficher = Listbox(club, height=5, width=80)
#         for i in range(len(liste_clubs)):
#             liste_clubs_afficher.insert(i, liste_clubs[i])
#         liste_clubs_afficher.grid(row=6, column=2)
    
#         def retour():
#             bouton_retour.destroy()
#             club.destroy()
#             Accueil()

#         #creer bouton retour vers l'accueil
#         bouton_retour = Button(club, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
#         bouton_retour.grid(row=18, column=2)

    
#         #afficher la fenetre
#         club.mainloop()

def Accueil():
        
        #creer une fenetre
        fenetre = Tk()

        #donner un titre a la fenetre
        fenetre.title("Arbitrage")

        #donner une taille a la fenetre
        #fenetre.geometry("1920x1080")
        #taille de la fenetre s'adapte a la taille de l'ecran
        fenetre.geometry("{0}x{1}+0+0".format(fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()))

        #mettre un logo a la fenetre
        fenetre.iconbitmap('Interface/img/logo2.ico')
        #logo = PhotoImage(file="Interface/img/logo2.png")
        # logo_label = Label(fenetre, image=logo)
        # logo_label.grid(row=0, column=0)

       
        #ajouter l'image comite.png a la fenetre en bas à droite
        comite = PhotoImage(file="Interface/img/comite.png")
        comite_label = Label(fenetre, image=comite)
        comite_label.place(x=1000,y=500,relwidth=0.5,relheight=0.5)
        #mettre une image en background a la fenetre
        background_image = PhotoImage(file="Interface/img/pingpong.png")
        background_label = Label(fenetre, image=background_image)
        background_label.place(x=725,y=150,relwidth=0.5,relheight=0.5)


        #couleur de fond de la fenetre
       # fenetre.configure(background='#DADAD7')


        def open_clubs():
            fenetre.destroy()
            os.system("python Interface/Clubs.py")


        def open_JA():
            fenetre.destroy()
            os.system("python Interface/JA.py")


        def open_teams():
            fenetre.destroy()
            os.system("python Interface/Equipes.py")
       
        
        def open_rencontres():
            fenetre.destroy()
            os.system("python Interface/Rencontres.py")
        

        def open_affectation():
           
            fenetre.destroy()
            os.system("python Interface/Affectations.py")
                        
        
        def quit():
            fenetre.destroy()
            

        #creer 6 boutons
        bouton_clubs = Button(fenetre, text="Clubs", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=open_clubs)
        bouton_JA = Button(fenetre, text="JA", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=open_JA)
        bouton_Équipes = Button(fenetre, text="Équipes", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=open_teams)
        bouton_Rencontres = Button(fenetre, text="Rencontres", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=open_rencontres)
        bouton_Affectation = Button(fenetre, text="Affectation JA", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'), command=open_affectation)
        bouton_Poules = Button(fenetre, text="Poules", bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'))
        bouton_Quitter = Button(fenetre, text="Quitter" , command=quit, bg='#FF5733', fg='#FFFFFF', font=('Helvetica', 10, 'bold'))

        #placer les boutons dans la fenetre
        bouton_clubs.grid(row=3, column=2)
        bouton_JA.grid(row=6, column=2)
        bouton_Équipes.grid(row=9, column=2)
        bouton_Rencontres.grid(row=12, column=2)
        bouton_Affectation.grid(row=15, column=2)
        bouton_Poules.grid(row=18, column=2)
        bouton_Quitter.grid(row=21, column=2)

        #taille des boutons
        bouton_clubs.config(height=5, width=80)
        bouton_JA.config(height=5, width=80)
        bouton_Équipes.config(height=5, width=80)
        bouton_Rencontres.config(height=5, width=80)
        bouton_Affectation.config(height=5, width=80)
        bouton_Poules.config(height=5, width=80)
        bouton_Quitter.config(height=5, width=80)

        #mettre un espace entre les boutons
        bouton_clubs.grid(padx=10, pady=10)
        bouton_JA.grid(padx=10, pady=10)
        bouton_Équipes.grid(padx=10, pady=10)
        bouton_Rencontres.grid(padx=10, pady=10)
        bouton_Affectation.grid(padx=10, pady=10)
        bouton_Poules.grid(padx=10, pady=10)
        bouton_Quitter.grid(padx=10, pady=10)


        #afficher la fenetre
        fenetre.attributes('-fullscreen', True)
        fenetre.mainloop()

Accueil()
