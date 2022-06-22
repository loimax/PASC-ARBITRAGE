from tkinter import *
import os
from utils import *
def JA():
        conn = create_connection("Interface/testdb/GestionRegionale.db")
        cursor = conn.cursor()
        #créer une fenetre
        Arb = Tk()
        #donner un titre
        Arb.title("JA")
        #donner une taille 
        #Arb.geometry("1920x1080")
        #taille de la fenetre s'adapte a la taille de l'ecran
        Arb.geometry("{0}x{1}+0+0".format(Arb.winfo_screenwidth(), Arb.winfo_screenheight()))

         #uptade de la liste des JA
        def update(data):
            #clear the listbox
            JA_list.delete(0, END)

            #ajpouter les JA dans la listbox
            for item in data:
                JA_list.insert(END, item)
        #afficher le JA séléctionné
        def fillout(e):
            entry_JA.delete(0, END)
            entry_JA.insert(0, JA_list.get(ANCHOR))

        #créer fonction entrée vs liste de JA
        def check(e):
            #grab what typed
            typed = entry_JA.get()

            if typed == '':
                data = liste_JA
            else:
                data = []
                for item in liste_JA:
                    if typed.lower() in item.lower():
                        data.append(item)

            update(data)

         #faire une fonction qui ouvre un formulaire pour ajouter un JA lorque on clique sur le bouton
        def add_JA():
            #créer une fenetre
            add_JA = Tk()
            #donner un titre a la fenetre
            add_JA.title("Ajouter un JA")
            #donner une taille a la fenetre
            add_JA.geometry("400x200")
            #couleur de fond de la fenetre
            add_JA.configure(background='#DADAD7')
            #créer une zone de texte pour les noms des JAs
            entry_numero_JA = Entry(add_JA, width=30)
            entry_numero_JA.grid(row=1, column=2)
            #créer une zone de texte pour les noms des JAs
            entry_nom_JA = Entry(add_JA, width=30)
            entry_nom_JA.grid(row=2, column=2)
            #créer une zone de texte pour les noms des JAs
            entry_prenom_JA = Entry(add_JA, width=30)
            entry_prenom_JA.grid(row=3, column=2)
            #créer une zone de texte pour les noms des JAs
            entry_club_JA = Entry(add_JA, width=30)
            entry_club_JA.grid(row=4, column=2)
            #créer une zone de texte pour les noms des JAs
            entry_adresse_JA = Entry(add_JA, width=30)
            entry_adresse_JA.grid(row=5, column=2)
            #créer une zone de texte pour les noms des JAs
            entry_cp_JA = Entry(add_JA, width=30)
            entry_cp_JA.grid(row=6, column=2)
            #créer une zone de texte pour les noms des JAs
            entry_ville_JA = Entry(add_JA, width=30)
            entry_ville_JA.grid(row=7, column=2)
            #créer une zone de texte pour le Tel du JA
            entry_tel_JA = Entry(add_JA, width=30)
            entry_tel_JA.grid(row=8, column=2)
            #afficher les titres des zones de texte
            label_numero = Label(add_JA, text="Numéro de Licence du JA :")
            label_numero.grid(row=1, column=1)
            label_nomJA = Label(add_JA, text="Nom du JA :")
            label_nomJA.grid(row=2, column=1)
            label_prenom_JA = Label(add_JA, text="Prenom :")
            label_prenom_JA.grid(row=3, column=1)
            label_clubJA = Label(add_JA, text="club :")
            label_clubJA.grid(row=4, column=1)
            label_adresse_JA = Label(add_JA, text="Adresse :")
            label_adresse_JA.grid(row=5, column=1)
            label_cp = Label(add_JA, text="cp :")
            label_cp.grid(row=6, column=1)
            label_ville = Label(add_JA, text="Ville :")
            label_ville.grid(row=7, column=1)
            label_tel = Label(add_JA, text="Tel :")
            label_tel.grid(row=8, column=1)
            #recuperer les données du formulaire
            def add_JA_data():
                numero_JA = entry_numero_JA.get()
                nom_JA = entry_nom_JA.get()
                prenom_JA = entry_prenom_JA.get()
                club_JA = entry_club_JA.get()
                adresse_JA = entry_adresse_JA.get()
                cp_JA = entry_cp_JA.get()
                ville_JA = entry_ville_JA.get()
                tel_JA = entry_tel_JA.get()
                # mettre les elements dans une liste
                print(numero_JA, nom_JA, prenom_JA, club_JA, adresse_JA, cp_JA, ville_JA, tel_JA)
                data = [numero_JA, nom_JA, prenom_JA, club_JA, adresse_JA, cp_JA, ville_JA, tel_JA]

                checkInsertModify(conn, cursor, "JA", data)
                # insert_entry("JA", data)
                add_JA.destroy()
                
                
        
                
            #créer un bouton pour valider les données
            button_valider = Button(add_JA, text="Valider",command=lambda : [add_JA_data()])
            button_valider.grid(row=8, column=2)
            
            
            

            


        def supprimer_JA():
            nom = JA_list.get(ANCHOR)
            print(nom)
            del_entry(conn, cursor, "JA", "NomJA", nom)
            

            #update(liste_JAs)

        def rafraichir():
            Arb.destroy()
            os.system("python Interface\JA.py")

        
        def modifier_JA():
            nom = JA_list.get(ANCHOR)
            print(nom)
            #on ouvre une fenetre
            modif_JA = Tk()
            #on donne un titre a la fenetre
            modif_JA.title("Modifier un JA")
            #on donne une taille a la fenetre
            modif_JA.geometry("400x200")
            #on crée un formulaire ou on affiche les données du JA séléctionné
            label_numero = Label(modif_JA, text="Numéro de Licence du JA :")
            label_numero.grid(row=1, column=1)
            label_nomJA = Label(modif_JA, text="Nom du JA :")
            label_nomJA.grid(row=2, column=1)
            label_prenom_JA = Label(modif_JA, text="Prénom du JA :")
            label_prenom_JA.grid(row=3, column=1)
            label_clubJA = Label(modif_JA, text="club :")
            label_clubJA.grid(row=4, column=1)
            label_adresse_JA = Label(modif_JA, text="adresse :")
            label_adresse_JA.grid(row=5, column=1)
            label_cp = Label(modif_JA, text="cp :")
            label_cp.grid(row=6, column=1)
            label_ville = Label(modif_JA, text="Ville :")
            label_ville.grid(row=7, column=1)
            label_tel = Label(modif_JA, text="Tel :")
            label_tel.grid(row=8, column=1)
            #on recupere les données du JA séléctionné
            data = getListRow(conn, cursor, "JA", ["NomJA"], [nom])
            #on les affiche dans le formulaire
            entry_numero_JA = Entry(modif_JA, width=30)
            entry_numero_JA.grid(row=1, column=2)
            entry_numero_JA.insert(END, data[0])
            entry_nom_JA = Entry(modif_JA, width=30)
            entry_nom_JA.grid(row=2, column=2)
            entry_nom_JA.insert(END, data[1])
            entry_prenom_JA = Entry(modif_JA, width=30)
            entry_prenom_JA.grid(row=3, column=2)
            entry_prenom_JA.insert(END, data[2])
            entry_club_JA = Entry(modif_JA, width=30)
            entry_club_JA.grid(row=4, column=2)
            entry_club_JA.insert(END, data[3])
            entry_adresse_JA = Entry(modif_JA, width=30)
            entry_adresse_JA.grid(row=5, column=2)
            entry_adresse_JA.insert(END, data[4])
            entry_cp_JA = Entry(modif_JA, width=30)
            entry_cp_JA.grid(row=6, column=2)
            entry_cp_JA.insert(END, data[5])
            entry_ville_JA = Entry(modif_JA, width=30)
            entry_ville_JA.grid(row=7, column=2)
            entry_ville_JA.insert(END, data[6])
            entry_tel_JA = Entry(modif_JA, width=30)
            entry_tel_JA.grid(row=8, column=2)
            entry_tel_JA.insert(END, data[7])

            def modif_JA_data():
                numero_JA = entry_numero_JA.get()
                nom_JA = entry_nom_JA.get()
                prenom_JA = entry_prenom_JA.get()
                club_JA = entry_club_JA.get()
                adresse_JA = entry_adresse_JA.get()
                cp_JA = entry_cp_JA.get()
                ville_JA = entry_ville_JA.get()
                tel_JA = entry_tel_JA.get()
                # mettre les elements dans une liste
                a = [numero_JA, nom_JA, prenom_JA, club_JA, adresse_JA, cp_JA, ville_JA, tel_JA]
                print(a)
                checkInsertModify(conn, cursor, "JA", a, True, nom)
                
                # modify_entry(conn, cursor, "JA", a, getID(data))
                # print(getListRow(conn, cursor, "JA", ["NomJA"], [nom]))
                # print(display_table(conn, cursor, "JA"))
                
            #mettre les elements dans une liste
            #mod = [entry_numero_JA, entry_nom_JA, entry_prenom_JA, entry_club_JA, entry_adresse_JA, entry_cp_JA, entry_ville_JA]
            #on crée un bouton pour valider les données
            button_valider = Button(modif_JA, text="Valider", command = lambda : [modif_JA_data(), modif_JA.destroy()])
            button_valider.grid(row=9, column=2)
            #,X
           # button_valider = Button(add_JA, text="Valider",command=lambda : [add_JA_data(), update(liste_JAs)])
            #button_valider.grid(row=8, column=2)
            
        
            


        #créer 3 boutons pour les JAs : modifier ajouter supprimer
        bouton_modifier = Button(Arb, text="Modifier", fg='#000000', font=('Arial', 10, 'bold'),command=modifier_JA)
        bouton_modifier.place(x=600, y=400)
        bouton_ajouter = Button(Arb, text="Ajouter", fg='#000000', font=('Arial', 10, 'bold'),command=add_JA)
        bouton_ajouter.place(x=725, y=400)
        bouton_supprimer = Button(Arb, text="Supprimer", fg='#000000', font=('Arial', 10, 'bold'), command=lambda : [supprimer_JA()])
        bouton_supprimer.place(x=850, y=400)
        bouton_rafraichir = Button(Arb, text="Rafraichir", fg='#000000', font=('Arial', 10, 'bold'),
                                  command=rafraichir)
        bouton_rafraichir.place(x=720, y=500)

        #creer une zone de texte pour la recherche de JA
        entry_JA = Entry(Arb, font=("Helvetica", 20))
        entry_JA.place(x=600, y=150)

        #créer une zone pour la liste de JA
        JA_list = Listbox(Arb, width=50)
        JA_list.place(x=600, y=200)

        #créer une liste de JA 
        #créer une liste de JA
        liste_JA = creation_liste(conn, cursor, "JA", "NomJA")
        # liste_JA = ["Nom 1", "Nom 2", "Nom 3", "Nom 4", "Nom 5", "Nom 6", "Nom 7", "Nom 8", "Nom 9", "Nom 10", "Nom 11", "Nom 12", "Nom 13", "Nom 14", "Nom 15", "Nom 16", "Nom 17", "Nom 18", "Nom 19", "Nom 20", "Nom 21", "Nom 22", "Nom 23", "Nom 24", "Nom 25", "Nom 26", "Nom 27", "Nom 28", "Nom 29", "Nom 30", "Nom 31", "Nom 32", "Nom 33", "Nom 34", "Nom 35", "Nom 36"]
        #Ajouter JA dans la liste
        update(liste_JA)

        #afficher le JA selectionné
        JA_list.bind("<<ListboxSelect>>", fillout)

        #create a binding to the entry box
        entry_JA.bind("<KeyRelease>", check)

    
        def retour():
            # bouton_retour.destroy()
            Arb.destroy()
            os.system("python Interface/Accueil.py")

        #creer bouton retour vers l'accueil
        bouton_retour = Button(Arb, text="Retour", command=retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_retour.place(x=725, y=700)

    
        #afficher la fenetre
        # Arb.attributes('-fullscreen', True)
        Arb.mainloop()

#afficher la fenetre
JA()