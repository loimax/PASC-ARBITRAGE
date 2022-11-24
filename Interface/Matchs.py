import os
from tkinter import *
from tkinter.ttk import Combobox
from Affectations import Affectation
from utils import *
from re import split


#window_height : 701, nope, dépends de la taille réelle de l'écran
#window_width : 1284, ça aussi

#faire un tableau avec des listes déroulantes pour choisir l"équipe

class Matchs():
    def __init__(self, liste_from_poules, niveau, poule, année=2022, phase=1):
        self.liste_debase_equipes = liste_from_poules
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

        # Liste des équipes dans le Cher (0418 au début de leur numClub)
        self.list_Cher = []
        # self.main_window.update()
        self.create_UI()
        #afficher la fenetre
        self.main_window.mainloop()



    def create_UI(self):
        #créer tableau qui hold les équipes
        self.add_phat_table()
        self.add_txt()


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
            self.hour_CB[i] = Combobox(self.main_window, values = ["9:30:00", "17:00:00"], font=("Arial", 12), justify=CENTER, width = 10)
            self.hour_CB[i].insert(END,"9:30:00")
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
            for j in range(4):
                if self.list_CB1[i][j].get()=="EXEMPT " or self.list_CB2[i][j].get()=="EXEMPT ":
                    print("EXEMPT rencontred")
                else:
                    string_split = split(' ', self.list_CB1[i][j].get())
                    string_split.pop()
                    num_eq1 = string_split.pop()
                    num_eq1 = num_eq1.replace(num_eq1[0], "")
                    num_eq1 = num_eq1.replace(num_eq1[len(num_eq1)-1], "")
                    rang_equipe1 = string_split.pop()
                    nom_club1 = ""
                    for debile in range(len(string_split)):
                        nom_club1 += (string_split[debile])
                        if debile != len(string_split)-1:
                            nom_club1 += " "
                    
                    string_split = split(' ', self.list_CB2[i][j].get())
                    string_split.pop()
                    num_eq2 = string_split.pop()
                    num_eq2 = num_eq2.replace(num_eq2[0], "")
                    num_eq2 = num_eq2.replace(num_eq2[len(num_eq2)-1], "")
                    rang_equipe2 = string_split.pop()
                    nom_club2 = ""
                    for marrant in range(len(string_split)):
                        nom_club2 += (string_split[marrant])
                        if marrant != len(string_split)-1:
                            nom_club2 += " "

                    #nom equipe rangEq (numEq)

                    num_club1 = getValues(self.conn,self.cursor,"CLUB","NumClub","NomClub",[nom_club1])
                    for a in num_club1:
                        pre_num_club1 = str(a[0:4])
                       
                    if pre_num_club1 == "0418":
                        phase = getValues(self.conn,self.cursor,"EquipeClub","Phase","NumEq",num_eq1)
                        insert_entry(self.conn,self.cursor,"Rencontres",[f"{num_eq1}",f"{num_eq2}",f"{phase[0]}",f"{i+1}",f"{self.list_date[i].get()}",f"{self.hour_CB[i].get()}",""],['NumEq1', 'NumEq2', 'Phase', 'Journee', 'DateRenc', 'HeureRenc', 'JA'])
                        self.list_Cher.append([nom_club1,nom_club2,getMaxValue(self.conn,self.cursor,"Rencontres","NumRenc")])
        self.test_if_Cher()


    def test_if_Cher(self):
        """
        On regarde si la liste contient des valeurs,
        si c'est le cas, c'est qu'on a des matchs à domicile dans le Cher
        On lance donc la fenêtre : affectation de juge-arbitre
        """
        if self.list_Cher == []:
            pass
        else:
            self.main_window.destroy()
            Affectation(self.list_Cher)




    def retour(self):
            # bouton_retour.destroy()
            self.main_window.destroy()
            close_connection(self.conn)
            os.system("python Interface/main.py")


    def quitter(self):
        close_connection(self.conn)
        self.main_window.destroy()


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