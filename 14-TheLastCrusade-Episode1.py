import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

grille = []

types = {}
types["0+TOP"] = "NULL"
types["0+LEFT"] = "NULL"
types["0+RIGHT"] = "NULL"
types["1+TOP"] = "DOWN"
types["1+LEFT"] = "DOWN"
types["1+RIGHT"] = "DOWN"
types["2+TOP"] = "NULL"
types["2+LEFT"] = "RIGHT"
types["2+RIGHT"] = "LEFT"
types["3+TOP"] = "DOWN"
types["3+LEFT"] = "NULL"
types["3+RIGHT"] = "NULL"
types["4+TOP"] = "LEFT"
types["4+LEFT"] = "NULL"
types["4+RIGHT"] = "DOWN"
types["5+TOP"] = "RIGHT"
types["5+LEFT"] = "DOWN"
types["5+RIGHT"] = "NULL"
types["6+TOP"] = "NULL"
types["6+LEFT"] = "RIGHT"
types["6+RIGHT"] = "LEFT"
types["7+TOP"] = "DOWN"
types["7+LEFT"] = "NULL"
types["7+RIGHT"] = "DOWN"
types["8+TOP"] = "NULL"
types["8+LEFT"] = "DOWN"
types["8+RIGHT"] = "DOWN"
types["9+TOP"] = "DOWN"
types["9+LEFT"] = "DOWN"
types["9+RIGHT"] = "NULL"
types["10+TOP"] = "LEFT"
types["10+LEFT"] = "NULL"
types["10+RIGHT"] = "NULL"
types["11+TOP"] = "RIGHT"
types["11+LEFT"] = "NULL"
types["11+RIGHT"] = "NULL"
types["12+TOP"] = "NULL"
types["12+LEFT"] = "NULL"
types["12+RIGHT"] = "DOWN"
types["13+TOP"] = "NULL"
types["13+LEFT"] = "DOWN"
types["13+RIGHT"] = "NULL"


# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    grille.append([])
    grille[i] = line.split()
    
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    direction = types[ str(grille[yi][xi]) + "+" + pos ]
    if  direction == "DOWN":
        yi += 1
    elif direction == "LEFT":
        xi -= 1
    else:
        xi += 1

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(str(xi) + " " + str(yi))
