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
          print("Plus de pioche !")
          return None


class Table:
    def __init__(self):
        self.pli = []
        self.compteur_passes = 0
    
    def __str__(self):
        return str(self.pli)
        
    def pli_actuel(self):
        return self.pli
    
    def surenchere(self, score):
        self.pli = score
    
    def fermer_pli(self):
        self.pli = []


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
            return "plus de cartes"
    
    def redistribution(self, pioche):
        self.main = []
        for _ in range(8):
            carte_haut_pioche = pioche.premiere_carte()
            self.main.append(carte_haut_pioche)
    
    def change_etat(self, etat):
        self.etat = etat
    
    def retire_vie(self):
        if self.vies == 2:
            self.vies -= 1
            print(f"\n---------------------------------------\nLe joueur {self.numero} a perdu la manche, il perd une vie.\n\n")
        elif self.vies == 1:
            self.vies -= 1
            print(f"\n---------------------------------------\nLe joueur {self.numero} a perdu la manche et la partie ! C'est un mauvais guide...")
    
    def en_vie(self):
        return self.vies > 0
    
    def passer(self, pioche, table, nb_joueurs):
        main_valeurs = []
        for carte in self.main:
            main_valeurs.append(carte.valeur)
            
        carte_haut_pioche = pioche.premiere_carte()
        
        if carte_haut_pioche != None:
            garder = ""
            while garder not in ['y','n']:
                garder = input(f"Carte piochée : {carte_haut_pioche.valeur}. Garder ? (y/n)")
            if garder=='y':
                indice = -1
                while indice==-1:
                    try:
                        print(main_valeurs)
                        indice = int(input(f"Où l'insérer ? (De 0 à {len(main_valeurs)-1})"))
                    except:
                        print("Mauvaise saisie, recommencer")
                self.main.insert(indice, carte_haut_pioche)
                print(f"Nouvelle main : {self}")
        
        print(f"\n{table.compteur_passes} joueurs ont passé leur tour")
        if table.compteur_passes == nb_joueurs-1:
                table.fermer_pli()
                print("Pli fermé")
            
    
    def calcul_force(self, liste_cartes):
        if liste_cartes==[]:
            return 0
        long=len(liste_cartes)
        chiffre=liste_cartes[0]
        resultat=0
        for i in range(long):
            resultat+=chiffre*(10**(i))
        return resultat
            
    def jouer(self, table, pioche, nb_joueurs):
        contrainte = self.calcul_force(table.pli_actuel())
        
        main_valeurs = []
        for carte in self.main:
            main_valeurs.append(carte.valeur)
        
        positions = ""
        cartes = None
        while cartes == None:
            positions = input(f"Position(s) de la (des) carte(s) à jouer ? (0 à {len(main_valeurs)-1}, séparées par des virgules sans espaces)\n(Si vous ne pouvez rien jouer, vous pouvez passer avec p) ").split(",")
            
            if positions==['p']:
                table.compteur_passes+=1
                self.passer(pioche, table, nb_joueurs)
                return None
            
            try:
                positions = list(map(int, positions))
                positions = sorted(positions)
                
                #Si tous les tests suivants sont bons, la variable choix garde cette valeur
                cartes = []
                for pos in positions:
                    cartes.append(main_valeurs[pos])
                
                #Test 1 : cartes choisies côte à côte ?
                for k in range(len(positions)-1):
                    if positions[k+1] != positions[k]+1:
                        print("Les cartes doivent être côte à côte")
                        cartes = None
                
                val = main_valeurs[positions[0]]
                
                #Test 2 : toutes les cartes de même valeur ? 
                for i in positions[1:]:
                    if main_valeurs[i] != val:
                        print("Valeur différente de la précédente")
                        cartes = None
                
                #Test 3 : valeur supérieure à celle sur la table ?
                if cartes != None:
                    force = self.calcul_force(cartes) 
                    if force <= contrainte:
                        print(f"Vous devez jouer au-dessus de {table.pli_actuel()}")
                        cartes = None
                
            except:
                print("Mauvaise saisie, recommencer")
                cartes = None
        
        print(f"Cartes jouées : {cartes}")
        self.main = [i for j, i in enumerate(self.main) if j not in positions]
        print(f"Nouvelle main : {self}")
        
        if table.pli_actuel() != []:
            garder = ""
            while garder not in ['y','n']:
                garder = input(f"Cartes sur la table : {table.pli}. Garder ? (y/n)")
            if garder=='y':
                indice = -1
                while indice==-1:
                    try:
                        indice = int(input(f"Où les insérer ? (De 0 à {len(self.main)-1})"))
                    except:
                        print("Mauvaise saisie, recommencer")
                for chiffre in table.pli:
                    self.main.insert(indice, Carte(chiffre))
                print(f"Nouvelle main : {self}")
            
        table.surenchere(cartes)
        table.compteur_passes=0
        return cartes
    
    def tour_de_jouer(self, table, pioche, nb_joueurs):
        print(f"Sur la table : {table}")
        
        main_valeurs = []
        for carte in self.main:
            main_valeurs.append(carte.valeur)
        print(f"Votre main : {self}")
        
        if table.pli_actuel()==[]:
            self.jouer(table, pioche, nb_joueurs)
        else:
            action = ""
            while action not in ['j','p']:
                action = input('Action ("j" pour jouer ou "p" pour passer) : ')
            if action=='j':
                self.jouer(table, pioche, nb_joueurs)
            elif action=='p':
                table.compteur_passes+=1
                self.passer(pioche, table, nb_joueurs)
    

if __name__=="__main__":
        
    pioche = Pioche()
    
    table = Table()
    
    manche = 0
    
    J1 = Joueur(1, pioche)
    J2 = Joueur(2, pioche)
    J3 = Joueur(3, pioche)
    J4 = Joueur(4, pioche)
    
    Joueurs_en_jeu = [J1,J2,J3,J4]
    
    perdant = 0

    
    """Boucle de jeu"""
    
    while (J1.en_vie() and J2.en_vie() and J3.en_vie() and J4.en_vie()) :
        manche+=1
        
        Joueurs_en_jeu = [J1,J2,J3,J4]
        
        print(f"-------------------------------\n#    Nouvelle manche : manche {manche}\n-------------------------------")
        print(f"#    Vies restantes :\nJ1 : {J1.vies} vies\nJ2 : {J2.vies} vies\nJ3 : {J3.vies} vies\nJ4 : {J4.vies} vies\n-------------------------------\n")
        
        num_joueur = 0
        if manche > 1:
            num_joueur = perdant-1
            print(f"Le perdant commence : joueur {perdant}")
            perdant = 0
        
        pioche = Pioche()
        table = Table()
        for joueur in Joueurs_en_jeu:
            joueur.change_etat("en jeu")
            joueur.redistribution(pioche)
        
        liste_num = []
        
        while len(Joueurs_en_jeu)>1:
            
            Joueur_actuel = Joueurs_en_jeu[(num_joueur)%len(Joueurs_en_jeu)]
            
            if Joueur_actuel.etat=="gagnant":
                tmp=liste_num.index(Joueur_actuel.numero)
                num_tmp=Joueur_actuel.numero
                Joueurs_en_jeu.remove(Joueur_actuel)    # retiré ici pour que si le joueur gagnant remporte le pli, le joueur suivant soit bien celui qui commence à jouer
                num_joueur = tmp % (len(Joueurs_en_jeu))
                Joueur_actuel = Joueurs_en_jeu[num_joueur]
                print(f"\n#    Le joueur {num_tmp}, gagnant, a quitté la manche. Il reste {len(Joueurs_en_jeu)} joueurs.")             
                if table.compteur_passes == len(Joueurs_en_jeu)-1:    # cas où le gagnant se retire de la table pendant que des joueurs passent leur tour sur un pli qui n'est pas celui du gagnant
                    table.fermer_pli()
                    print("\nPli fermé")
            
            liste_num = []
            for j in Joueurs_en_jeu:
                liste_num.append(j.numero)
            print(f"\n---------------------------------------\nManche {manche}, joueurs en jeu : {liste_num}")
            
            if len(Joueurs_en_jeu)==1:
                Joueur_actuel.change_etat("perdant")
                perdant = Joueur_actuel.numero
                Joueur_actuel.retire_vie()    
            else:            
                print(f"---------------------------------------\nAu tour du joueur {Joueur_actuel.numero}\n---------------------------------------")
                Joueur_actuel.tour_de_jouer(table, pioche, len(Joueurs_en_jeu))
            
                if Joueur_actuel.main==[]:
                        Joueur_actuel.change_etat("gagnant")
                        print(f"Joueur {Joueur_actuel.numero} : {Joueur_actuel} et {Joueur_actuel.etat}")
                        num_joueur+=1
                else:        
                    num_joueur+=1
                    
    print("-------------------------------\n#    Fin du jeu\n-------------------------------")