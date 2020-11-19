#Alles wird importiert
from time import sleep
from random import randint
#Alle Listen werden erstellt
liste_br = ['B','Br','Bl','D','Dr','Fr','Fl','F','St','Sp','Sch','S','H','M','N']
liste_eu = ['eu','au','e','a','i','o','u','ei','ie']
liste_fl = ['fl','ch','pf','g','n','m','f','g','d','b','mt','r','s']
liste_22 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,              22,23,24,25,26,27,28,
            29,30,31,32,33,
            34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,
            52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
liste_fm = ['B','Br','Bl','D','Dr','Fr','Fl','F','St','Sp','Sch','S','H','M','N']
liste_ei = ['o','eu','au','e','a','i','u','ei','ie']
liste_ft = ['f','n','m','g','d','b','mt','r','s']
#Die Funktion zum erstellen des Passwortes
def Passworterstellen():

    zufall_1 = randint(1,2)
    i = 0
    while i<zufall_1:
      bef = [liste_br[randint(0,14)], 
      liste_eu[randint(0,8)],
      liste_fl[randint(0,12)]]
        #print
        #print
        #print
      i = i+1


    zahl = liste_22[randint(0,99)]


    zufall_2 = randint(1,2)
    i = 0
    while i<zufall_2:
      fef = [liste_fm[randint(0,14)],
      liste_ei[randint(0,8)],
      liste_ft[randint(0,5)]]
      #print
      #print
      #print
      i = i+1

    print(bef[0], bef[1], bef[2], zahl , fef[0], fef[1], fef[2])

    
    #ausgeben = [eins,zwei,drei,zahl,vier,fuenf,sechs]
    #uninteressant = " "

    #ausgeben_eins = 
    
    #ausgeben_eins = ausgeben[0] + ausgeben[1] + ausgeben[2] 
    
    #ausgeben_zahl = ausgeben[3]

    #ausgeben_zwei = ausgeben[4] + ausgeben[5] + ausgeben[6]

    #ausgeben_zwei = ausgeben[1]
    #ausgeben_drei = ausgeben[2]
    #ausgeben_vier = ausgeben[3]
    #ausgeben_fuenf = ausgeben[4]
    #ausgeben_sechs = ausgeben[5]
    #ausgeben_sieben = ausgeben[6]

  #ausgeben = ausgeben_eins

  #ausgeben_eins = uninteressant.split()
  #ausgeben_zwei = uninteressant.split()
  #ausgeben_drei = uninteressant.split()
  #ausgeben_vier = uninteressant.split()
  #ausgeben_fuenf = uninteressant.split()
  #ausgeben_sechs = uninteressant.split()
  #ausgeben_sieben = uninteressant.split()
  
  #alles = [ausgeben[]]
  

    #print(ausgeben_eins , ausgeben_zahl , ausgeben_zwei)
    
    #keineAhnung = ["Hallo","Hello","hallo","hello"]
    #print(keineAhnung[0])
    #Regel 1
    #zufall = randint(8,15)
    #zufall1 = randint(0,zufall)
    #zufall2 = randint(0,zufall1)
    #zufall3 = randint(0,zufall2)
    #zufall4 = randint(0,zufall3)
    #zufall5 = randint(0,zufall4)
    
    
    #i = 0
    #e2 = 'ä'
    #while i < zufall:
     #   e1 = liste_br[randint(0,6)]
      #  while e1 == e2:
       #     e1 = liste_br[randint(0,6)]
        #print(e1)
        #i = i+1
        #e2 = e2
#Der Hauptcode indem alle Funktionen aufgerufen werden




Passworterstellen()