##############################################################################
#
# A simple example of some of the features of the XlsxWriter Python module.
#
# Copyright 2013-2020, John McNamara, jmcnamara@cpan.org
#
import sqlite3
import xlsxwriter
import sys
from datetime import date,time

def format_copy_add(fmt,param=dict()):
    '''
    Réalise la copie d'un format (fmt) avec ajout de propriétés (param)
    '''
    # Récupération des propriétés spécifiques au format
    properties = [f[4:] for f in dir(fmt) if f[0:4] == 'set_']
    # Création d'un format de base pour récupérer les paramètres initiaux
    dft_fmt = workbook.add_format()
    dict_param = {k : v for k, v in fmt.__dict__.items() if k in properties and dft_fmt.__dict__[k] != v}
    for k, v in param.items():
        dict_param[k] = v
    return workbook.add_format(dict_param)

def rapport_recap(rencontres):
    '''
    Prépare le fichier xlsx pour le JA contenant convocation et rapport sur deux feuilles différentes POUR UNE SEULE RENCONTRE
    '''

    ############################################################################
    #
    #             CREATION DU FICHIER ET DES FORMATS DE CELLULES
    #
    ############################################################################
    
    global workbook
    titreWBK = "Recapitulatif-JA.xlsx"
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(titreWBK)
    
    # Par défaut, c'est de l'Arial, on souhaite mettre du 'Times New Roman', donc tous les
    # styles auront cet attribut changé.
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})
    # style de base 
    normal_format = workbook.add_format({'align': 'left','valign':'vcenter',
                                        'font_size':12})
    # Cellules avec taille 10
    normal10_format = format_copy_add(normal_format,{'font_size':10})
    # Cellules centrées
    center_format = format_copy_add(normal_format,{'align':'center'})
    # Cellules alignées à droite
    right_format = format_copy_add(normal_format,{'align':'right'})
    right10_format = format_copy_add(right_format,{'font_size':10})

    # Cellules pour mettre en gras
    bold_format = format_copy_add(normal_format,{'bold':True})
    # Cellules pour mettre en gras taille 9
    bold9_format = format_copy_add(bold_format,{'font_size':9})
    bold9I_format = format_copy_add(bold9_format,{'italic':True,'align':'center'})
    # Cellules pour mettre en gras taille 10
    bold10_format = format_copy_add(bold_format,{'font_size':10})
    bold12_format = format_copy_add(bold_format,{'font_size':12,'align':'center'})

    # Cellules encadrées fin
    squared1_format = format_copy_add(normal_format,{'border':1,'align':'center','border_color':'#3A3A3A'})
    # Cellules encadrées Gras
    squared1B_format = format_copy_add(squared1_format,{'bold':True})
    # Cellules encadrées épais HGD
    squared2TLR_format = format_copy_add(squared1_format,{'top':2,'left':2,'right':2,'bottom':0})
    # Cellules encadrées épais BGD
    squared2BLR_format = format_copy_add(squared1_format,{'top':0,'left':2,'right':2,'bottom':2})
    # Cellules pointillés droite
    squared3_format = format_copy_add(squared1_format,{'top':0,'left':0,'right':3,'bottom':0,'font_size':10})
    # Cellules encadrées titre
    squared6_format = format_copy_add(squared1_format,{'border':6,'bold':True})
    # Cellules du bas de feuille
    merge_bottom_format = format_copy_add(squared1_format,{'top':6,'left':0,'right':0,'bottom':0,'align':'center','valign':'bottom','bold':True})
    # Cellules pour mettre en gras centré encadré (éventuellement italique)
    squared2BC_format = format_copy_add(squared1_format,{'top':0,'left':2,'right':2,'bottom':0,'align':'center','bold':True})
    squared2BIC_format = format_copy_add(squared2BC_format,{'italic':True})
    squared2BC_format.set_font_size(10)
    # Encadrement Frais
    squared2Black_format = format_copy_add(squared1_format,{'border_color':'black','border':2})
    # Cellules encadrées titre rempli
    squared6BG_format = format_copy_add(squared6_format,{'pattern':17,'bold':False,'border_color':'black','font_size':10})
    
    # Cellules COVID (en rouge)
    red_bold_format = format_copy_add(bold_format, {'font_color':'red'})

    # Cellules grises....
    gray_cells = workbook.add_format()
    gray_cells.set_bg_color('gray')

    date_format = workbook.add_format({'align': 'left'})
    date_format.set_num_format('dd/mm/yyyy')
    date_format.set_font_name('Times New Roman')
    date_format.set_font_size(10)
    date8_format = format_copy_add(date_format,{'align':'right','font_size':8})

    hour_format = workbook.add_format({'align': 'left'})
    hour_format.set_num_format('hh" heures "mm')
    hour_format.set_font_name('Times New Roman')
    hour_format.set_font_size(10)



    #############################################################################
    #
    #             Récapitulatif par date
    #
    ##############################################################################

    # Mise en page (impression)
    worksheet = workbook.add_worksheet("Récapitulatif par date")
    worksheet.set_landscape()
    worksheet.set_margins(left=0.4,right=0.4,top=0.4,bottom=0.4)
    worksheet.set_paper(9)
    worksheet.center_vertically()
    worksheet.center_horizontally()
    worksheet.print_area(0,0,40,16)
#    worksheet.hide_gridlines(2)

    worksheet.write('A1', 'Phase',bold12_format)
    worksheet.write('B1', 'Journée',bold12_format)
    worksheet.write('C1', 'Date',bold12_format)
    worksheet.write('D1', 'Division + Poule',bold12_format)
    worksheet.write('E1', 'Equipe Recevante',bold12_format)
    worksheet.write('F1', 'Equipe Reçue',bold12_format)
    worksheet.write('G1', 'Juge Arbitre',bold12_format)


    ligne = 1


    # Format the column to make the text clearer.
    worksheet.set_column('A:B', 9)
    worksheet.set_column('C:C', 12)
    worksheet.set_column('D:D', 6)
    worksheet.set_column('E:F', 30)
    worksheet.set_column('G:G', 25)
    worksheet.set_column('H:H', 30)
    worksheet.set_column('I:I', 15)
#    for i in range(43):
#        worksheet.set_row(i, 12.75)

#    print(rencontres)
    nbParJA = {}
    nbParClub = {}
    clubJA = {}
    for renc in rencontres:
        ligne = ligne + 1
        print (renc)
#0 (1, 
#1 '26/09/2021', 
#2 'R3', 
#3 'E', 
#4 'CP BIGNY VALLENAY', 
#5  1, 
#6 'TT GERMINOIS', 
#7  2, 
#8 'BERGERON', 
#9 'Gaëlle')
# CREATE VIEW ALlRencontres AS
# SELECT journee, DateRenc,  Eq1.division, Eq1.poule, 
#       Club1.NomClub, Eq1.RangEq, 
# 	   club2.NomClub, Eq2.RangEq, nomJA, prenomJA

        Phase = 1
        Journee = renc[0]
        if (Journee > 7):
              Journee = Journee - 7
              Phase = 2
        DateRenc = renc[1]
        DivPoule = renc[2] + " " + renc [3]
        EqRecev  = renc[4] + " (" + str(renc[5]) + ")"
        EqRecue  = renc[6] + " (" + str(renc[7]) + ")"
        JA       = " "
        try:
            JA       = renc[8] + " " + renc[9]
        except:
            None

        worksheet.write('A' + str(ligne), Phase ,center_format)
        worksheet.write('B' + str(ligne), Journee ,center_format)
        worksheet.write('C' + str(ligne) , DateRenc, center_format)
        worksheet.write('D' + str(ligne), DivPoule, center_format)        
        worksheet.write('E' + str(ligne), EqRecev, center_format) 
        worksheet.write('F' + str(ligne), EqRecue, center_format) 
        worksheet.write('G' + str(ligne), JA, center_format) 


 






    

    #############################################################################
    #
    #             REMPLISSAGE DES DONNEES
    #
    ##############################################################################

 

    workbook.close()





#############################################################################
#
#             RECUPERATION DES DONNEES DES RENCONTRES
#
#   format de l'appel:
#   python3.8 testXlsxWriter.py optNumJournee optNumRencontre
#          - optNumJournee: pour sortir les rencontres de la journée en question
#                           par défaut 1
#          - optNumRencontre: pour sélectioner une rencontre précise 
#                           par défaut toutes
#
##############################################################################



# Par défaut la première journée : on peut préciser le numero de journée 
# en premier argument

req = """
SELECT * FROM AllRencontres ;
"""



# Vérification de la requête.
# print(req)

saison = "2021/2022"
cnx = sqlite3.connect("GestionRegionale.db")
cur = cnx.cursor()
cur.execute(req)

rows = cur.fetchall()
rapport_recap(rows)



    
