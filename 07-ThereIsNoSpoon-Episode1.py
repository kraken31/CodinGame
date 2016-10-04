import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
grille = []

for i in range(height):
    line = input()  # width characters, each either 0 or .
    grille.append([])
    for j in range(width):
        grille[i].append(line[j])
        
for i in range(height):
    for j in range(width):
        if grille[i][j] == "0":
            
            resultat = str(j) + " " + str(i) + " "
            trouve_x = 0
            cpt_x = j+1
            
            # Recherche du noeud x voisin
            while trouve_x == 0 and cpt_x < width:
                if grille[i][cpt_x] == "0":
                    trouve_x = 1
                    resultat += str(cpt_x) + " " + str(i) + " "
                else:
                    cpt_x += 1
            if trouve_x == 0:
                resultat += "-1 -1 "
                
            # Recherche du noeud y voisin
            trouve_y = 0
            cpt_y = i+1
            while trouve_y == 0 and cpt_y < height:
                if grille[cpt_y][j] == "0":
                    trouve_y = 1
                    resultat += str(j) + " " + str(cpt_y)
                else:
                    cpt_y += 1
            if trouve_y == 0:
                resultat += "-1 -1"
                
            print(resultat)

                
                    
            # Recherche du noeud y voisin
            
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# Three coordinates: a node, its right neighbor, its bottom neighbor
