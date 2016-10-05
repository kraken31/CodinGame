import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
base_x = 0
top_x = w -1
base_y = 0
top_y = h - 1

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if "U" in bomb_dir:
        top_y = y0
        y0 = base_y + ((y0 - base_y) // 2)
    
    if "R" in bomb_dir:
        base_x = x0
        x0 = top_x - ((top_x - x0) // 2)

    if "D" in bomb_dir:
        base_y = y0
        y0 = top_y - ((top_y - y0) // 2)

    if "L" in bomb_dir:
        top_x = x0
        x0 = base_x + ((x0 - base_x) // 2)
        
    # the location of the next window Batman should jump to.
    print(str(x0) + " " + str(y0))
