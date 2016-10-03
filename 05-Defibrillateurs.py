import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()

lon_cur = float(lon.replace(',','.'))
lat_cur = float(lat.replace(',','.'))
dist_min = 0
defib_min = ""

n = int(input())
for i in range(n):
    defib = input()
    infos_defib = defib.split(';')
    
    lon_defib = float(infos_defib[4].replace(',','.'))
    lat_defib = float(infos_defib[5].replace(',','.'))
    
    x = (lon_defib - lon_cur) * math.cos( (lat_cur + lat_defib)/2 )
    y = (lat_defib - lat_cur)
    distance = math.sqrt(x**2 + y**2) * 6371
    
    if i == 0:
        dist_min = distance
        defib_min = infos_defib[1]
    elif distance < dist_min:
        dist_min = distance
        defib_min = infos_defib[1]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(defib_min)
