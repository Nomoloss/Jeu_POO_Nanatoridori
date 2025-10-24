# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 09:07:59 2025

@author: Formation
"""

import numpy as np


class Carte:
    def __init__(self, valeur):
        self.valeur = valeur


class Pioche:
    def __init__(self):
        self.cartes = []
        for _ in range(9):
            for k in range(1,8):
                self.cartes.append(Carte(k))
        rng = np.random.default_rng()
        rng.shuffle(self.cartes)
    
    def __str__(self):
        liste = []
        for carte in self.cartes:
            liste.append(carte.valeur)
        return str(liste)
    
    def __len__(self):
        return len(self.cartes)
    
    def premiere_carte(self):
        try:
          carte=self.cartes.pop(0)
          return carte
        except:
          return None


class Table:
    def __init__(self):
        self.pli = 0
        
    def pli_actuel(self):
        return self.pli
    
    def surenchere(self, score):
        self.pli = score
    
    def fermer_pli(self):
        self.pli = 0


class Joueur:
    def __init__(self, numero, pioche):
        self.numero = numero
        self.main = []
        for _ in range(8):
            carte_haut_pioche = pioche.premiere_carte()
            self.main.append(carte_haut_pioche)
        self.etat = "en jeu" #"en jeu", "gagnant" ou "perdant"
        self.vies = 2
    
    def __str__(self):
        if len(self.main) > 0:
            liste = []
            for carte in self.main:
                liste.append(carte.valeur)
            return str(liste)
        else:
            return self.etat
    
    def change_etat(self, etat):
        self.etat = etat
    
    def retire_vie(self):
        self.vies -= 1
    
    def en_vie(self):
        return self.vies > 0
    
    def commande_valide(self, positions):
            
            
            
            
            
            
            
            
            
    
    def passer(self, pioche):
        carte_haut_pioche = pioche.premiere_carte()
        if carte_haut_pioche != None:
            self.main.append(carte_haut_pioche)
            
    def jouer(self, table):
        contrainte = table.pli_actuel()
        
        main_valeurs = []
        for carte in self.main:
            main_valeurs.append(carte.valeur)
        
        choix = ""
        while choix 
            choix = input(f"Position(s) de la (des) carte(s) à jouer ? (0 à {len(main_valeurs)}, séparées par des virgules)")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        return choix
    
    def tour_de_jouer(self, pioche):
        action = ""
        while action not in ['j','p']:
            action = input('Action ("j" pour jouer ou "p" pour passer) : ')
        if action=='j':
            self.jouer()
        elif action=='p':
            self.passer(pioche)
    

if __name__=="__main__":
        
    pioche = Pioche()
    #print(pioche)
    table = Table()
    
    manche = 0
    
    # premier_joueur = 0
    # while premier_joueur not in ['1','2','3','4']:
    #     premier_joueur = input('Premier joueur (1, 2, 3 ou 4) : ')
    
    """
    ###########################################################
    '
    '       A EFFACER SI PAS UTILISE   (les 3 lignes au-dessus)
    '
    ###########################################################
    """
    
    Joueur_1 = Joueur(1, pioche)
    Joueur_2 = Joueur(2, pioche)
    Joueur_3 = Joueur(3, pioche)
    Joueur_4 = Joueur(4, pioche)
    
    print(Joueur_1)
    print(Joueur_2)
    print(Joueur_3)
    print(Joueur_4)
    print(f"{len(pioche)} cartes restantes dans la pioche")
    
    
    """Boucle de jeu"""
    
    while (Joueur_1.en_vie() and Joueur_2.en_vie() and Joueur_3.en_vie() and Joueur_4.en_vie()) :
        manche+=1
        Joueur_1.change_etat("en jeu")
        Joueur_2.change_etat("en jeu")
        Joueur_3.change_etat("en jeu")
        Joueur_4.change_etat("en jeu")
        
        if manche == 1:
            Joueur_1.jouer(table)
            print("fin")
            break
            
            
            




test = [2, 3, 3, 3, 6, 3, 7, 6]
print(test)
positions = ""
cartes = None
while cartes == None:
    positions = input(f"Position(s) de la (des) carte(s) à jouer ? (0 à {len(test)-1}, séparées par des virgules sans espaces) ").split(",")
    positions = list(map(int, positions))
    
    
    
    
    
    #faire une fonction (commande_valide) de ce bloc en-dessous : mettre 
    #des return False pour faire sortir 
    
    try:
        for k in range(len(positions)-1):
            if positions[k+1] != positions[k]+1:
                print("pas croissant de un en un")
                #return False
            
        
        
        
        
        # en-dessous ça marche :
        val = test[positions[0]]
        print(f"{positions[0]}e position = {val}")
        cartes = positions
        
        for i in positions[1:]:
            print(f"{i}e position = {test[i]}")
            if test[i] != val:
                print("valeur différente")
                cartes = None #<- provisoire, mettre qqch pour refaire boucler le while
    except:
        print("Mauvaise saisie, recommencer")
    
    
        


