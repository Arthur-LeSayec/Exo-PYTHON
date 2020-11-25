def initialiseGrille (grille): 
    compteur = 0
    for compteur in range (0, 8) :
        grille [compteur] = "_"
    return grille

def afficherGrille (grille):
    i=0
    for i in range (0, 2) :
        print(grille[3*i], grille[3*i+1], grille[3*i+2], "\n")
    return grille

def ajouteSymbole (grille):
    i=0
    choixIncorrect = True
    while (choixIncorrect):
        print("Sur quelle ligne voulez-vous jouez?")
        input(i)
        print("Sur quelle colonne voulez-vous jouez ?")
        input(j)
        if (grille[3*i+j]!="_"):
            grille[3*i+j]=joueur
            choixIncorrect=False
    return()

def testeVictoireVerticale (grille):
    compteur = 0
    while (compteur <3):
        if (grille[compteur]!="_" and grille[compteur] == grille[compteur +3] and grille[compteur] == grille [compteur +6]):
            return True
    return False

def testeVictoireHorizontale (grille):
    compteur=0
    while(compteur <3):
        if (grille[compteur]!="_" and grille[compteur*3]==grille[compteur*3+1] and grille[compteur*3]==grille[compteur*3+2]):
            return True
    return False

def testeVictoireDiagonale (grille):
    if (grille[compteur]!="_" and grille[4]== grille[0] and grille[4]== grille[8]):
        return True
    if (grille[compteur] !="_" and grille[4]==grille[2] and grille[4]==grille[6]):
        return True
    return False

def testeJeuNul(gagnantTrouvé):
    if(tour==9 and gagnantTrouvé==False):
        return True
    return False


input()
        