import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
d = message.encode()
resultat_binaire = ""
for i in d:
    resultat_binaire += bin(i)[2:].zfill(7)

# Conversion en unaire
last_num = ""
nb_num = ""
resultat_unaire = ""

for i in resultat_binaire:
    if i == last_num:
        nb_num += "0"
    else:
        resultat_unaire += nb_num
        if resultat_unaire != "":
            resultat_unaire += " "
            
        nb_num = "0"
        if i == "1":
            last_num = "1"
            resultat_unaire += "0 "
        else:
            last_num = "0"
            resultat_unaire += "00 "
            
resultat_unaire += nb_num

print(resultat_unaire)
