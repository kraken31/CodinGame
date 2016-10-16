import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
val_max = 0
val_min = 0
perte = 0

n = int(input())
for i in input().split():
    v = int(i)
    
    if val_max == 0 and val_min == 0:
        val_max = v
        val_min = v
    elif v > val_max:
        val_max = v
        val_min = v
    elif v < val_min:
        val_min = v
    
    if perte < val_max - val_min:
        perte = val_max - val_min

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(perte*-1)
