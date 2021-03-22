# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 02:30:23 2021

@author: cmayi
"""
import taquin

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
    for k in etatsExplores:
        if(k==taquin):
            print("Cet état a déjà été visité.\n")
            break
        else:
            etatsExplores.append(taquin)
    return etatsExplores
        
    etatsExplores.append(taquin)
    
def heuristique(taquin):
    h=[]
    
    for k in range(0,6):
        j=0
        for i in range(0,8):
             j = j+(poids[k][i]*distElem(taquin)[i])
        j= j//coeff[k]
        h.append(j)
    return h
def fctEval(taquin):
    g=sum(distElem(taquin))
    h= heuristique(taquin)[5] #manhattan
    fctEval = g+h
    return fctEval

