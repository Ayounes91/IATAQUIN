# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 02:30:23 2021

@author: cmayi
"""
import taquin
#from taquin import afficher


#Poids et coefficients
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

def distElem(a):
    x1 = a.index("1")
    x2 = a.index("2")
    x3 = a.index("3")
    x4 = a.index("4")
    x5 = a.index("5")
    x6 = a.index("6")
    x7 = a.index("7")
    x8 = a.index("8")
    xn = a.index("X")
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

def etatsExplores(memoire,a):
    etatsExplores = []
    for k in etatsExplores:
        if(k==a):
            return False
            #Cet état a déjà été visité.
            break
        else:
            etatsExplores.append(a)
    return etatsExplores
        
   
    
def heuristique(a):
    h=[]
    
    for k in range(0,6):
        j=0
        for i in range(0,8):
             j = j+(poids[k][i]*distElem(a)[i])
        j= j//coeff[k]
        h.append(j)
    return h

def fctEval(a):
    g=sum(distElem(a))
    h= heuristique(a)[5] #manhattan
    fctEval = g+h
    return fctEval

def trouGauche(a):
    Xn = a.index("X")
    if(not(Xn in [0,3,6])):
       a[Xn] = a[Xn-1]
       a[Xn-1] = "X"
    return a

def trouDroit(a):
    Xn = a.index("X")
    if(not(Xn in [2,5,8])):
       a[Xn] = a[Xn+1]
       a[Xn+1] = "X"
    return a

def trouHaut(a):
    Xn = a.index("X")
    if(not(Xn in [0,1,2])):
       a[Xn] = a[Xn-3]
       a[Xn-3] = "X"
    return a

def trouBas(a):
    Xn = a.index("X")
    if(not(Xn in [6,7,8])):
       a[Xn] = a[Xn+3]
       a[Xn+3] = "X"
    return a
def nxtState(a):
    
    Xn = a.index("X")
    if(Xn==0):
        r1 = trouDroit(a)
        r2 = trouBas(a)
        nxtState = [r1,r2]
        for k in nxtState:
            if etatsExplores(k,memoire)==False:
                nxtState.delete(k)
        evalState = []
        for k in nxtState:
            evalState.append(fctEval(k))
        for k in nxtState:
            if fctEval(k)==min(evalState):
                return k
    if(Xn==1):
        r1 = trouDroit(a)
        r2 = trouBas(a)
        r3 = trouGauche(a)
        nxtState = [r1,r2,r3]
        evalState = []
        for k in nxtState:
            if etatsExplores(k,memoire)==False:
                nxtState.delete(k)
        for k in nxtState:
            evalState.append(fctEval(k))
        for k in nxtState:
            if fctEval(k)==min(evalState):
                return k     
    if(Xn==2):
        r1 = trouGauche(a)
        r2 = trouBas(a)
        nxtState = [r1,r2]
        evalState = []
        for k in nxtState:
            if etatsExplores(k,memoire)==False:
                nxtState.delete(k)
        for k in nxtState:
            evalState.append(fctEval(k))
        for k in nxtState:
            if fctEval(k)==min(evalState):
                return k
    if(Xn==3):
        r1 = trouDroit(a)
        r2 = trouBas(a)
        r3 = trouHaut(a)
        nxtState = [r1,r2,r3]
        evalState = []
        for k in nxtState:
            if etatsExplores(k,memoire)==False:
                nxtState.delete(k)
        for k in nxtState:
            evalState.append(fctEval(k))
        for k in nxtState:
            if fctEval(k)==min(evalState):
                return k 
    if(Xn==4):
        r1 = trouDroit(a)
        r2 = trouBas(a)
        r3 = trouHaut(a)
        r4 = trouGauche(a)
        nxtState = [r1,r2,r3,r4]
        evalState = []
        for k in nxtState:
            if etatsExplores(k,memoire)==False:
                nxtState.delete(k)
        for k in nxtState:
            evalState.append(fctEval(k))
        for k in nxtState:
            if fctEval(k)==min(evalState):
                return k
    if(Xn==5):
        r1 = trouGauche(a)
        r2 = trouBas(a)
        r3 = trouHaut(a)
        nxtState = [r1,r2,r3]
        evalState = []
        for k in nxtState:
            if etatsExplores(k,memoire)==False:
                nxtState.delete(k)
        for k in nxtState:
            evalState.append(fctEval(k))
        for k in nxtState:
            if fctEval(k)==min(evalState):
                return k  
    if(Xn==6):
        r1 = trouDroit(a)
        r2 = trouHaut(a)
        nxtState = [r1,r2]
        evalState = []
        for k in nxtState:
            if etatsExplores(k,memoire)==False:
                nxtState.delete(k)
        for k in nxtState:
            evalState.append(fctEval(k))
        for k in nxtState:
            if fctEval(k)==min(evalState):
                return k 
    if(Xn==7):
        r1 = trouDroit(a)
        r2 = trouGauche(a)
        r3 = trouHaut(a)
        nxtState = [r1,r2,r3]
        evalState = []
        for k in nxtState:
            if etatsExplores(k,memoire)==False:
                nxtState.delete(k)
        for k in nxtState:
            evalState.append(fctEval(k))
        for k in nxtState:
            if fctEval(k)==min(evalState):
                return k
    if(Xn==8):
        r1 = trouGauche(a)
        r2 = trouHaut(a)
        nxtState = [r1,r2]
        evalState = []
        for k in nxtState:
            if etatsExplores(k,memoire)==False:
                nxtState.delete(k)
        for k in nxtState:
            evalState.append(fctEval(k))
        for k in nxtState:
            if fctEval(k)==min(evalState):
                return k
    

memoire = []

def auto():
    taq = taquin.melanger()
    i=0 #Compteur de coups joués
    chemin=[]
    
    while(not(taquin.victoire(taq,[1,2,3,4,5,6,7,8,"X"],i,chemin))):
        taq = nxtState(taq)
        taquin.afficher(taq)
        i = i+1
        
        
        
