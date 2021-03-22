# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 00:04:13 2021

@author: cmayi
"""
import random
from random import randint #Pour générer des chiffres aléatoirement
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
    print("Distances élémentaires :",distElem(taquin))
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
    

def melanger():
    chiffres=[1,2,3,4,5,6,7,8,"X"] #On cherche à générer un taquin à partir
                                    #d'un taquin déjà résolu
    i=0
    deplacement = ["2","4","6","8"]
    
    while(i<randint(25,150)):
        Xn = chiffres.index("X")
        rep = random.choice(deplacement)
        if(rep=="8"):
            if(Xn not in [0,1,2]): #Si la case vide est sur le bord supérieur du taquin
                       #Sinon
                chiffres[Xn] = chiffres[Xn-3] #Monter la case vide revient à la faire se déplacer 3 cases
                chiffres[Xn-3] = "X"                       #Vers l'arrière
        elif(rep=="2"):
            if(Xn not in [6,7,8]): #Si la case vide est sur le bord inférieur du taquin
                    #Sinon
                chiffres[Xn] = chiffres[Xn+3] #Descendre la case vide revient à la faire se déplacer 3 cases
                chiffres[Xn+3] = "X"                       #En avant
        elif(rep=="4"): #Pour aller à gauche
            if(Xn not in [0,3,6]): #Si la case vide est sur le bord gauche du taquin
               
                chiffres[Xn] = chiffres[Xn-1] #Sinon cela revient à la reculer d'une case 
                chiffres[Xn-1] = "X"
        elif(rep=="6"):#Pour aller à droite
            if(Xn not in [2,5,8]): #Si la case est sur le bord droit du taquin
               
                chiffres[Xn] = chiffres[Xn+1] #Sinon cela revient à l'avancer d'une case
                chiffres[Xn+1] = "X" 
        i = i+1
    return chiffres
def distElem(taquin):
    x1 = taquin.index(1)
    x2 = taquin.index(2)
    x3 = taquin.index(3)
    x4 = taquin.index(4)
    x5 = taquin.index(5)
    x6 = taquin.index(6)
    x7 = taquin.index(7)
    x8 = taquin.index(8)
    xn = taquin.index("X")
    d1 = abs(x1-0) # abs = valeur absolue
    d2 = abs(x2-1)
    d3 = abs(x3-2)
    d4 = abs(x4-3)
    d5 = abs(x5-4)
    d6 = abs(x6-5)
    d7 = abs(x7-6)
    d8 = abs(x8-7)
    dx = abs(xn-8)
    return [d1,d2,d3,d4,d5,d6,d7,d8,dx]

def etatsExplores(taquin):
    etatsExplores = []
    etatsExplores.append(taquin)
pi1=[36,12,12,4,1,1,4,1,0]
pi2=[8,7,6,5,4,3,2,1,0]
pi3=pi2
pi4=[8,7,6,5,3,2,4,1,0]
pi5=pi4
pi6=[1,1,1,1,1,1,1,1,0]
poids =[pi1,pi2,pi3,pi4,pi5,pi6]
rho1=4
rho3=rho1
rho5=rho1
rho2=1
rho4=rho2
rho6=rho2
coeff=[rho1,rho2,rho3,rho4,rho5,rho6]
def manhattan(taquin):
    h=[]
    
    for k in range(0,6):
        j=0
        for i in range(0,8):
             j = j+(poids[k][i]*distElem(taquin)[i])
        j= j//coeff[k]
        h.append(j)
   
            
def main():
    taquin = melanger()
    i=0 #Compteur de coups joués
    chemin=[]
    while(not(victoire(taquin,[1,2,3,4,5,6,7,8,"X"],i,chemin))): #Tant qu'on ne résout pas le taquin
        jouer(taquin,chemin)                                   #Le jeu continue
        i = i+1
        
