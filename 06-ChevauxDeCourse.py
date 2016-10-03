import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
puissances = []
for i in range(n):
    pi = int(input())
    puissances.append(pi)

puissances.sort()
delta_min = -1

for i in range(1, n):
    delta = puissances[i] - puissances[i-1]
    if delta < delta_min or delta_min < 0:
        delta_min = delta
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(delta_min)
