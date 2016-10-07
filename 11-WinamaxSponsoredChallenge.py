import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
joueur1 = []
joueur2 = []
pot_joueur1 = []
pot_joueur2 = []

n = int(input())  # the number of cards for player 1
for i in range(n):
    
    cardp_1 = input()  # the n cards of player 1
    cardp_1 = cardp_1[:-1]
    
    carte = 0
    if cardp_1[0] == "J":
        carte = 11
    elif cardp_1[0] == "Q":
        carte = 12
    elif cardp_1[0] == "K":
        carte = 13
    elif cardp_1[0] == "A":
        carte = 14
    else:
        carte = int(cardp_1)
    
    joueur1.append(carte)
        
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    cardp_2 = cardp_2[:-1]

    carte = 0
    if cardp_2[0] == "J":
        carte = 11
    elif cardp_2[0] == "Q":
        carte = 12
    elif cardp_2[0] == "K":
        carte = 13
    elif cardp_2[0] == "A":
        carte = 14
    else:
        carte = int(cardp_2)
    
    joueur2.append(carte)

fin = False
nb_manche = 0
while fin == False:
    
    if joueur1[0] > joueur2[0]:
        # Joueur 1 gagne
        nb_manche += 1
        
        joueur1 += pot_joueur1
        joueur1.append(joueur1[0])
        joueur1 += pot_joueur2
        joueur1.append(joueur2[0])
        del(joueur1[0])
        del(joueur2[0])
        del(pot_joueur1[:])
        del(pot_joueur2[:])
        
        if len(joueur2) == 0:
            fin = True
            resultat = "1 " + str(nb_manche) 

    elif joueur1[0] < joueur2[0]:
        # Joueur 2 gagne
        nb_manche += 1
        
        joueur2 += pot_joueur1
        joueur2.append(joueur1[0])
        joueur2 += pot_joueur2
        joueur2.append(joueur2[0])
        del(joueur1[0])
        del(joueur2[0])
        del(pot_joueur1[:])
        del(pot_joueur2[:])
        
        if len(joueur1) == 0:
            # Joueur 2 gagne
            fin = True
            resultat = "2 " + str(nb_manche) 
    else:
        # Bataille
        if len(joueur1) < 5 or len(joueur2) < 5:
            fin = True
            resultat = "PAT"
        else:
            pot_joueur1 += joueur1[0:4]
            pot_joueur2 += joueur2[0:4]
            del(joueur1[0:4])
            del(joueur2[0:4])
        
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(resultat)
