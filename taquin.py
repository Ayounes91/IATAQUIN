# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 00:04:13 2021

@author: cmayi
"""
import random #Pour générer des chiffres aléatoirement
def afficher(taquin):
    print(taquin)
    print(taquin[0],"|",taquin[1],"|",taquin[2])
    print("__|___|__")
    print(taquin[3],"|",taquin[4],"|",taquin[5])
    print("__|___|__")
    print(taquin[6],"|",taquin[7],"|",taquin[8])
    print("__|___|__")
def victoire(taquin,solution,i,chemin):
    if(taquin==solution):
        afficher(taquin)
        print("Félicitations !\n")
        print("Partie remportée en",i,"coups")
        print("Historique du chemin\n",chemin)
        return True
def jouer(taquin,chemin):
    afficher(taquin)
    Xn = taquin.index("X") #On stocke la position du X
    print("Que voulez-vous faire ?")
    rep = input("Monter (8)|Descendre (2)|Gauche (4)|Droite (6) ")
    chemin.append(pathConv.get(int(rep)))
    if(rep=="8"):
        if(Xn in [0,1,2]): #Si la case vide est sur le bord supérieur du taquin
            print("Impossible de déplacer en haut.") #Impossible de la déplacer
        else:        #Sinon
            taquin[taquin.index("X")] = taquin[Xn-3] #Monter la case vide revient à la faire se déplacer 3 cases
            taquin[Xn-3] = "X"                       #Vers l'arrière
    elif(rep=="2"):
        if(Xn in [6,7,8]): #Si la case vide est sur le bord inférieur du taquin
            print("Impossible de déplacer en bas.") #Impossible de la déplacer
        else:        #Sinon
            taquin[taquin.index("X")] = taquin[Xn+3] #Descendre la case vide revient à la faire se déplacer 3 cases
            taquin[Xn+3] = "X"                       #En avant
    elif(rep=="4"): #Pour aller à gauche
        if(Xn in [0,3,6]): #Si la case vide est sur le bord gauche du taquin
            print("Impossible de déplacer à gauche.") #Impossible de la déplacer
        else:
            taquin[Xn] = taquin[Xn-1] #Sinon cela revient à la reculer d'une case 
            taquin[Xn-1] = "X"
    elif(rep=="6"):#Pour aller à droite
        if(Xn in [2,5,8]): #Si la case est sur le bord droit du taquin
            print("Impossible de déplacer à droite.") #Impossible de la déplacer
        else:
            taquin[Xn] = taquin[Xn+1] #Sinon cela revient à l'avancer d'une case
            taquin[Xn+1] = "X"        
    else:
        print("Erreur de saisie.")

pathConv ={
    2:"Bas",
    4:"Gauche",
    6:"Droite",
    8:"Haut"}
    
def generer():
    chiffres = [1,2,3,4,5,6,7,8,"X"]
    c1 = random.choice(chiffres) #On génère les chiffres aléatoirement parmi ceux de la liste ci-dessus
    chiffres.remove(c1) #On retire les chiffres de la liste au fur et à mesure pour ne pas les générer à nouveau
    c2 = random.choice(chiffres)
    chiffres.remove(c2)
    c3 = random.choice(chiffres)
    chiffres.remove(c3)
    c4 = random.choice(chiffres)
    chiffres.remove(c4)
    c5 = random.choice(chiffres)
    chiffres.remove(c5)
    c6 = random.choice(chiffres)
    chiffres.remove(c6)
    c7 = random.choice(chiffres)
    chiffres.remove(c7)
    c8 = random.choice(chiffres)
    chiffres.remove(c8)
    c0 = random.choice(chiffres)
    chiffres.remove(c0)
    return [c1,c2,c3,c4,c5,c6,c7,c8,c0] #On constitue le taquin ainsi formé

def main():
    taquin = generer()
    i=0 #Compteur de coups joués
    chemin=[]
    while(not(victoire(taquin,[1,2,3,4,5,6,7,8,"X"],i,chemin))): #Tant qu'on ne résout pas le taquin
        jouer(taquin,chemin)                                   #Le jeu continue
        i = i+1
        
