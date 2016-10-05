import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
graphe = {}
passerelles = []

n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    if n1 in graphe.keys():
        graphe[n1].append(n2)
    else:
        graphe[n1] = [n2]
        
    if n2 in graphe.keys():
        graphe[n2].append(n1)
    else:
        graphe[n2] = [n1]
    
for i in range(e):
    ei = int(input())  # the index of a gateway node
    passerelles.append(ei)

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    
    # Parcours du graphe en prenant pour sommet l'emplacement de si
    # On crée une liste des noeuds rencontrés, dès qu'une passerelle est trouvée on coupe l'accès
    passerelle_trouve = 0
    liste_noeud = [si]
    while passerelle_trouve == 0 and len(liste_noeud) > 0:
        sommet = liste_noeud[0]
        for i in range(len(graphe[sommet])):
            if graphe[sommet][i] in passerelles:
                print (str(sommet) + " " + str(graphe[sommet][i]))
                passerelle_trouve = 1
            else:
                liste_noeud.append(graphe[sommet][i])
        
        # On supprime le sommet
        liste_noeud.pop(0)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # Example: 0 1 are the indices of the nodes you wish to sever the link between
