import os
from tkinter import *
from tkinter.ttk import Combobox
from utils import *
from JA import JA


#window_height : 701, nope, dépends de la taille réelle de l'écran
#window_width : 1284, ça aussi

#faire un tableau avec des listes déroulantes pour choisir l"équipe

class Matchs():
    def __init__(self, liste_from_poules, niveau, poule, année=2022, phase=1):
        self.liste_debase_equipes = liste_from_poules
        print("match list = " + str(self.liste_debase_equipes))
        self.conn = create_connection("Interface/testdb/GestionRegionale.db")
        self.cursor = self.conn.cursor()
        self.niveau = niveau
        self.poule = poule
        self.année = année
        self.phase = phase
        #créer une fenetre
        self.main_window = Tk()
        #donner un titre a la Matchs
        self.main_window.title("Matchs")

        self.main_window.attributes('-fullscreen', True)
        #donner une taille a la Matchs
        #self.main_window.geometry("1920x1080")
        #taille de la fenetre s'adapte a la taille de l'écran
        self.main_window.geometry("{0}x{1}+0+0".format(self.main_window.winfo_screenwidth(), self.main_window.winfo_screenheight()))

        self.list_date = []
        self.hour_CB = []
        self.list_CB1 = []
        self.list_CB2 = []
        

        #créer une liste d'équipes et les afficher 
        self.dates_rencontres = ["25/09/2021", "02/10/2021", "23/10/2021", "06/11/2021", "13/11/2021", "27/11/2021", "11/12/2021"]


        # self.main_window.update()
        # print(txt.winfo_width())
        self.create_UI()
        #afficher la fenetre
        self.main_window.mainloop()



    def create_UI(self):
        #créer tableau qui hold les équipes
        self.add_phat_table()
        self.add_txt()


    def mix_teams(self, list, i):
        tmp_list = []
        match i:
            case 0:
                tmp_list.append(list[0])
                tmp_list.append(list[1])
                tmp_list.append(list[2])
                tmp_list.append(list[3])
                tmp_list.append(list[7])
                tmp_list.append(list[6])
                tmp_list.append(list[5])
                tmp_list.append(list[4])
                return tmp_list
            
            case 1:
                tmp_list.append(list[6])
                tmp_list.append(list[5])
                tmp_list.append(list[4])
                tmp_list.append(list[7])
                tmp_list.append(list[0])
                tmp_list.append(list[1])
                tmp_list.append(list[2])
                tmp_list.append(list[3])
                return tmp_list

            case 2:
                tmp_list.append(list[0])
                tmp_list.append(list[1])
                tmp_list.append(list[2])
                tmp_list.append(list[7])
                tmp_list.append(list[5])
                tmp_list.append(list[4])
                tmp_list.append(list[3])
                tmp_list.append(list[6])
                return tmp_list

            case 3:
                tmp_list.append(list[4])
                tmp_list.append(list[3])
                tmp_list.append(list[2])
                tmp_list.append(list[5])
                tmp_list.append(list[0])
                tmp_list.append(list[1])
                tmp_list.append(list[7])
                tmp_list.append(list[6])
                return tmp_list

            case 4:
                tmp_list.append(list[0])
                tmp_list.append(list[1])
                tmp_list.append(list[6])
                tmp_list.append(list[7])
                tmp_list.append(list[3])
                tmp_list.append(list[2])
                tmp_list.append(list[4])
                tmp_list.append(list[5])
                return tmp_list

            case 5:
                tmp_list.append(list[2])
                tmp_list.append(list[1])
                tmp_list.append(list[3])
                tmp_list.append(list[4])
                tmp_list.append(list[0])
                tmp_list.append(list[7])
                tmp_list.append(list[6])
                tmp_list.append(list[5])
                return tmp_list

            case 6:
                tmp_list.append(list[0])
                tmp_list.append(list[6])
                tmp_list.append(list[5])
                tmp_list.append(list[7])
                tmp_list.append(list[1])
                tmp_list.append(list[2])
                tmp_list.append(list[3])
                tmp_list.append(list[4])
                return tmp_list


    def add_phat_table(self):
        nb_rencontres = 7
        nb_matchs_jour = 4
        eref = Entry(self.main_window, font=("Arial", 12), width=12, justify=CENTER)
        eref2 = Entry(self.main_window, font=("Arial", 12), width=5, justify=CENTER)
        eref.place(x=0, y=0)
        eref2.place(x=0, y=0)
        self.main_window.update()
        e_size = eref.winfo_width()
        e_sizeh = eref.winfo_height()
        num_journee_size = eref2.winfo_width()
        eref.destroy()
        eref2.destroy()
        for i in range(nb_rencontres):
            #CB pour les heures
            self.hour_CB.append(Combobox())
            self.hour_CB[i] = Combobox(self.main_window, values = ["9:30", "17:00"], font=("Arial", 12), justify=CENTER, width = 10)
            self.hour_CB[i].insert(END,"9:30")
            #self.hour_CB[j].place(x = 0, y = 0)

            tmp_list_CB1 = []
            tmp_list_CB2 = []
            for j in range(nb_matchs_jour):

                
                if (j == 0):
                    self.list_date.append(Entry(self.main_window, font=("Arial", 12), width=12, justify=CENTER))
                    self.list_date[i].place(x=0, y=0)
                    self.list_date[i].insert(END,self.dates_rencontres[i])
                    #self.list_date[i].config(state="disabled")
                    num_journee = Entry(self.main_window, font=("Arial", 12), width=5, justify=CENTER)
                    num_journee.place(x=0, y=0)
                    num_journee.insert(END,i+1)
                    num_journee.config(state="disabled")

                tmp_list_CB1.append(Combobox(self.main_window, values=self.liste_debase_equipes, font=("Arial", 12)))
                tmp_list_CB1[j].place(x=0, y=0)
                tmp_list_CB1[j].insert(END,self.mix_teams(self.liste_debase_equipes,i)[j])
                # tmp_list_CB1[j].config(state='disabled')

                tmp_list_CB2.append(Combobox(self.main_window, values=self.liste_debase_equipes, font=("Arial", 12)))
                tmp_list_CB2[j].place(x=0, y=0)
                tmp_list_CB2[j].insert(END,self.mix_teams(self.liste_debase_equipes,i)[j+4])
                # tmp_list_CB2[j].config(state='disabled')

                


                self.main_window.update()
                tab_len = e_size + num_journee_size + tmp_list_CB1[j].winfo_width() + tmp_list_CB2[j].winfo_width()+50
                start_array = self.main_window.winfo_width()/2-(tab_len)+25
                offset_top = 100
                if(i >= 4):
                    if (j == 0):
                        self.list_date[i].place(x=start_array+tab_len, y=offset_top+j*e_sizeh+(i-4)*140)
                        num_journee.place(x=start_array+e_size+tab_len, y=offset_top+j*e_sizeh+(i-4)*140)
                    if (j == 1):
                        self.hour_CB[i].place(x=start_array+tab_len, y=offset_top+j*e_sizeh+(i-4)*140)
                    tmp_list_CB1[j].place(x=start_array+e_size+num_journee_size+tab_len, y=offset_top+j*e_sizeh+(i-4)*140)
                    tmp_list_CB2[j].place(x=start_array+e_size+num_journee_size+tmp_list_CB1[j].winfo_width()+tab_len, y=offset_top+j*e_sizeh+(i-4)*140)
                else:
                    if (j == 0): 
                        self.list_date[i].place(x=start_array, y=offset_top+j*e_sizeh+i*140)
                        num_journee.place(x=start_array+e_size, y=offset_top+j*e_sizeh+i*140)
                    if (j == 1):
                        self.hour_CB[i].place(x=start_array, y=offset_top+j*e_sizeh+i*140)
                    tmp_list_CB1[j].place(x=start_array+e_size+num_journee_size, y=offset_top+j*e_sizeh+i*140)
                    tmp_list_CB2[j].place(x=start_array+e_size+num_journee_size+tmp_list_CB1[j].winfo_width(), y=offset_top+j*e_sizeh+i*140)

            self.list_CB1.append(tmp_list_CB1)
            self.list_CB2.append(tmp_list_CB2)



    def add_txt(self):
        txt = Label(self.main_window, text="Voici la feuille de match pour la poule " + self.poule + " de " + self.niveau + " - " + self.année + " phase " + self.phase, font=("Arial", 18))
        bouton_creer = Button(self.main_window, text="Créer", command=self.creer, bg='#AF7AC5', fg='#000000', font=('Arial', 12))
        bouton_retour = Button(self.main_window, text="Retour", command=self.retour, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))
        bouton_quitter = Button(self.main_window, text="Quitter", command=self.quitter, bg='#AF7AC5', fg='#000000', font=('Arial', 10, 'bold'))

        #pre-place objects
        txt.place(x = 0, y = 0)
        bouton_creer.place(x = 0, y = 0)
        bouton_retour.place(x = 0, y = 0)
        bouton_quitter.place(x = 0, y = 0)

        self.main_window.update()

        #placement des widgets en fonction de la fenetre
        txt.place(x = self.main_window.winfo_width()/2-txt.winfo_width()/2, y = 40)
        bouton_creer.place(x = self.main_window.winfo_width()/2-bouton_creer.winfo_width()/2, y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
        bouton_retour.place(x = 0.02*self.main_window.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())
        bouton_quitter.place(x = 0.98*self.main_window.winfo_width()-bouton_retour.winfo_width(), y = self.main_window.winfo_height()-0.04*self.main_window.winfo_height())


    def creer(self):
        for i in range(7):
            print(self.hour_CB[i].get())
            print(self.list_date[i].get())
            print(i)
            print("\n")
            for j in range(4):
                print("Match :  ")
                print(self.list_CB1[i][j].get())
                print(" VS ")
                print(self.list_CB2[i][j].get())
                print(f"|{self.list_CB1[i][j].get()}|")
                
                rang_equipe1 = self.list_CB1[i][j].get()[len(self.list_CB1[i][j].get())-1]
                nom_club1 = str(self.list_CB1[i][j].get()[:-2])  
                print("Nom ",nom_club1," rang : ",rang_equipe1) 
                rang_equipe2 = self.list_CB2[i][j].get()[len(self.list_CB2[i][j].get())-1]
                nom_club2 = str(self.list_CB2[i][j].get()[:-2])  
                print("Nom ",nom_club2," rang : ",rang_equipe2) 
                num_club1 = getValues(self.conn,self.cursor,"CLUB","NumClub","NomClub",[nom_club1])
                num_club2 = getValues(self.conn,self.cursor,"CLUB","NumClub","NomClub",[nom_club2])
                print(f"numéros des clubs : {num_club1} , {num_club2}")

                num_team1 = getValuesConstraints(self.conn,self.cursor,"EquipeClub","NumEq",["NumClub","RangEq"],[num_club1[0],rang_equipe1])
                num_team2 = getValuesConstraints(self.conn,self.cursor,"EquipeClub","NumEq",["NumClub","RangEq"],[num_club2[0],rang_equipe2])
                print(f"Numéros des équipes : {num_team1},{num_team2}")

                phase = getValues(self.conn,self.cursor,"EquipeClub","Phase","NumEq",num_team2)
                print(f"Numéros des phases : {phase}")
                # Petit bloque immonde parce que phase[0] est out if index pour une raison qui m'échappe
                for a in phase:
                    nani_phase = a
                for b in num_team1:
                    nani_team1 = b
                for c in num_team2:
                    nani_team2 = c

                insert_entry(self.conn,self.cursor,"Rencontres",[f"{nani_team1}",f"{nani_team2}",f"{nani_phase}",f"{i+1}",f"{self.list_date[i].get()}",f"{self.hour_CB[i].get()}",""],['NumEq1', 'NumEq2', 'Phase', 'Journee', 'DateRenc', 'HeureRenc', 'JA'])

                print("Match :  " + self.list_CB1[i][j].get() + " VS " + self.list_CB2[i][j].get())
            print("\nNew tab\n")
        liste_a_envoyer = []
        self.main_window.destroy()
        JA(liste_a_envoyer)



    def retour(self):
            # bouton_retour.destroy()
            self.main_window.destroy()
            os.system("python Interface/main.py")


    def quitter(self):
        self.main_window.destroy()