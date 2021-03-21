import math
import copy
from random import randint
import time


# CONSTANTES


POIDS = ((36, 12, 12, 4, 1, 1, 4, 1, 0),  # pi1
         (8, 7, 6, 5, 4, 3, 2, 1, 0),  # pi2 = pi3
         (8, 7, 6, 5, 3, 2, 4, 1, 0),  # pi4 = pi5
         (1, 1, 1, 1, 1, 1, 1, 1, 0))  # pi6

COEFF = (4, 1)



# CLASSES ET METHODES


class Taquin:
    """Liste des attributs

    taille : au moins 3
    etat : représentation matricielle par des couples ((abs,ord), valeur)
    Le trou est codé par la valeur maximale (taille*taille - 1)
    chemin : liste des mouvements du trou pour parvenir á l'état courant.
    N, S, E, O représentent respectivement Nord, Sud, Est, Ouest.
    Exemples de chemins : 'OSSOSNEEN', 'E', '' (chaîne vide pr état initial)
    cout : cout du chemin actuel. Correspond au nombre de déplacements
    f : fonction d'évaluation pour A*. f = cout + distanceManhattan
    """

    def __init__(self, n):
        self.taille = n
        self.etat = {(j // n, j % n): j for j in range(n * n)}
        self.chemin = ""
        self.cout = 0
        self.f = 0

    def afficher(self):
        for i in range(self.taille):
            liste = []
            for c in range(self.taille):
                liste.append(self.etat[i, c])
            print(liste)

    def victoire(self):
        #Renvoie True si le taquin est résolu.
        return self.etat == Taquin(self.taille).etat

    def chercher(self, e):
        #Retourne les coordonnées de la case e
        for i in range(self.taille):
            for j in range(self.taille):
                if self.etat[(i, j)] == e:
                    return (i, j)

    def bouger(self, direction):
        #Déplace le trou dans l'une des directions et renvoi le chemin

        copietaquin = copy.deepcopy(self)
        trou = self.chercher(len(self.etat) - 1)
        if direction == "N":
            copietaquin.etat[trou] = self.etat[(trou[0] - 1, trou[1])]
            copietaquin.etat[(trou[0] - 1, trou[1])] = self.etat[trou]
            copietaquin.chemin += "N"
        elif direction == "S":
            copietaquin.etat[trou] = self.etat[(trou[0] + 1, trou[1])]
            copietaquin.etat[(trou[0] + 1, trou[1])] = self.etat[trou]
            copietaquin.chemin += "S"
        elif direction == "E":
            copietaquin.etat[trou] = self.etat[(trou[0], trou[1] + 1)]
            copietaquin.etat[(trou[0], trou[1] + 1)] = self.etat[trou]
            copietaquin.chemin += "E"
        elif direction == "O":
            copietaquin.etat[trou] = self.etat[(trou[0], trou[1] - 1)]
            copietaquin.etat[(trou[0], trou[1] - 1)] = self.etat[trou]
            copietaquin.chemin += "O"
        else:
            print("Mouvement non reconnu. Devrait être N, S, E ou O.")
            print("Ça n'est pas censé se produire.")

        copietaquin.cout += 1
        return copietaquin

    def melanger_taquin(self):
        #Prend un taquin aleatoire et le melange
        trou = list(self.chercher(len(self.etat) - 1))

        for i in range(10000):
            trouHaut = (trou[0] == 0)
            trouBas = (trou[0] == self.taille - 1)
            trouGauche = (trou[1] == 0)
            trouDroite = (trou[1] == self.taille - 1)
            trouHG = trouHaut and trouGauche
            trouHD = trouHaut and trouDroite
            trouBG = trouBas and trouGauche
            trouBD = trouBas and trouDroite

            x = randint(1, 12)
            if trouHG:
                if x <= 6:
                    self = self.bouger("E")
                    trou[1] += 1
                else:
                    self = self.bouger("S")
                    trou[0] += 1
            elif trouHD:
                if x <= 6:
                    self = self.bouger("O")
                    trou[1] -= 1
                else:
                    self = self.bouger("S")
                    trou[0] += 1
            elif trouBG:
                if x <= 6:
                    self = self.bouger("E")
                    trou[1] += 1
                else:
                    self = self.bouger("N")
                    trou[0] -= 1
            elif trouBD:
                if x <= 6:
                    self = self.bouger("O")
                    trou[1] -= 1
                else:
                    self = self.bouger("N")
                    trou[0] -= 1
            elif trouHaut:
                if x <= 4:
                    self = self.bouger("O")
                    trou[1] -= 1
                elif 4 < x <= 8:
                    self = self.bouger("S")
                    trou[0] += 1
                else:
                    self = self.bouger("E")
                    trou[1] += 1
            elif trouBas:
                if x <= 4:
                    self = self.bouger("O")
                    trou[1] -= 1
                elif 4 < x <= 8:
                    self = self.bouger("N")
                    trou[0] -= 1
                else:
                    self = self.bouger("E")
                    trou[1] += 1
            elif trouGauche:
                if x <= 4:
                    self = self.bouger("N")
                    trou[0] -= 1
                elif 4 < x <= 8:
                    self = self.bouger("E")
                    trou[1] += 1
                else:
                    self = self.bouger("S")
                    trou[0] += 1
            elif trouDroite:
                if x <= 4:
                    self = self.bouger("N")
                    trou[0] -= 1
                elif 4 < x <= 8:
                    self = self.bouger("O")
                    trou[1] -= 1
                else:
                    self = self.bouger("S")
                    trou[0] += 1
            else:
                if x <= 3:
                    self = self.bouger("N")
                    trou[0] -= 1
                elif 3 < x <= 6:
                    self = self.bouger("E")
                    trou[1] += 1
                elif 6 < x <= 9:
                    self = self.bouger("S")
                    trou[0] += 1
                else:
                    self = self.bouger("O")
                    trou[1] -= 1

        # on réinitialise les valeurs car bouger_trou les change
        self.cout = 0
        self.f = 0
        self.chemin = ""
        return self

    def expanser(self):
        #Renvoie une liste des états accessibles à partir de l'état actuel

        trou = self.chercher(len(self.etat) - 1)

        trouN = (trou[0] == 0)
        trouS = (trou[0] == self.taille - 1)
        trouO = (trou[1] == 0)
        trouE = (trou[1] == self.taille - 1)
        trouNO = trouN and trouO
        trouNE = trouN and trouE
        trouSO = trouS and trouO
        trouSE = trouS and trouE

        eNord, eSud, eOuest, eEst = None, None, None, None

        if trouNO:
            eEst = self.bouger("E")
            eSud = self.bouger("S")
        elif trouNE:
            eOuest = self.bouger("O")
            eSud = self.bouger("S")
        elif trouSO:
            eNord = self.bouger("N")
            eEst = self.bouger("E")
        elif trouSE:
            eNord = self.bouger("N")
            eOuest = self.bouger("O")
        elif trouN:
            eEst = self.bouger("E")
            eSud = self.bouger("S")
            eOuest = self.bouger("O")
        elif trouS:
            eNord = self.bouger("N")
            eEst = self.bouger("E")
            eOuest = self.bouger("O")
        elif trouO:
            eNord = self.bouger("N")
            eSud = self.bouger("S")
            eEst = self.bouger("E")
        elif trouE:
            eNord = self.bouger("N")
            eSud = self.bouger("S")
            eOuest = self.bouger("O")
        else:
            eNord = self.bouger("N")
            eSud = self.bouger("S")
            eEst = self.bouger("E")
            eOuest = self.bouger("O")

        return [eNord, eSud, eOuest, eEst]

    def dist_elem(self, e):
        """Renvoie le nombre de cases séparant l'élément e de sa position
        voulue. Fonction intermédiaire pour la distance de Manhattan."""

        d = 0
        position_actuelle = self.chercher(e)
        position_voulue = (e // self.taille, e % self.taille)
        d = abs(position_actuelle[0] - position_voulue[0]) \
            + abs(position_actuelle[1] - position_voulue[1])
        return d

    def dist_manhattan(self, k):
        """Calcul de la distance Manhattan avec les POIDS[k] et les COEFF[k].
        Fonction intermédiaire pour la fonction d'évaluation f."""
        elem = [self.dist_elem(i) for i in range(len(self.etat))]
        elem = tuple(elem)
        if self.taille < 3:
            return sum(POIDS[k][i] * elem[i] \
                       for i in range(len(self.etat))) / COEFF[k % 2]
        else:
            poids = tuple([len(self.etat) - i - 1 for i in range(len(self.etat))])
            return sum(poids[i] * elem[i] \
                       for i in range(len(self.etat))) / COEFF[k % 2]

    def calculer_f(self, k):
        return self.cout + self.dist_manhattan(k)


class Frontiere:
    #Liste d'états triés selon leur valeur de f (ordre croissant)

    def __init__(self):
        self.etats = []

    def ajouter(self, e):
        #Ajoute e à la bonne position en fonction de sa valeur de f
        if self.etats == []:
            self.etats.insert(0, e)
        else:
            fait = False
            for i in range(len(self.etats)):
                if self.etats[i].f >= e.f and not fait:
                    self.etats.insert(i, e)
                    fait = True
            if not fait:
                self.etats.insert(len(self.etats), e)


class Etatsexplores:
    #Arbre binaire de recherche qui contient les états explorés

    def __init__(self):
        self.etats = []

    def ajouter(self, e):
        self.etats.append(e)

    def contient(self, e):
        for i in self.etats:
            if e.etat == i.etat:
                return True
        return False



# ALGORITHME A*


def main():
    # Initialisation =====================================================
    t = Taquin(3)
    ponderation = int(input("Pondération pour les distances de Manhattan (0 à 5) : "))
    t.afficher()

    t = t.melanger_taquin()  # pour avoir un taquin non résolu

    frontiere = Frontiere()
    frontiere.ajouter(t)
    memoire = Etatsexplores()  # crée l'ensemble des états déjà explorés

    if t.victoire():
        print("Le taquin est déjà solution.")
        return ""

    start_time = time.time()
    # Boucle principale =================================================
    while not t.victoire():

        if len(frontiere.etats) == 0:
            return "Frontière vide : pas de solution"

        t = frontiere.etats.pop(0)
        if t.victoire():
            print("recherche terminée en %s secondes" % (time.time() - start_time))
            print("solution : " + str(t.chemin))

            print(str(len(memoire.etats)) + " états explorés")

        expansion = t.expanser()  # On récupère une liste des états accessibles
        memoire.ajouter(t)
        for i in range(len(expansion)):
            if not expansion[i] == None:
                expansion[i].f = expansion[i].calculer_f(ponderation)
                if not memoire.contient(expansion[i]):
                    frontiere.ajouter(expansion[i])
        print("Etape suivante : ")
        t.afficher()
    return (None)

