import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
plane_first_x = 0
plane_first_y = 0
plane_last_x = 0
plane_last_y = 0
trouve = False
surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    #print(str(i) + ":" + str(land_x) + "," + str(land_y), file=sys.stderr)
    if i == 0:
        plane_first_x = land_x
        plane_first_y = land_y
    elif land_y == plane_first_y and trouve == False:
        plane_last_x = land_x
        plane_last_y = land_y
        trouve = True
    elif trouve == False:
        plane_first_x = land_x
        plane_first_y = land_y

#print("Plane = " + str(plane_first_x) + "," + str(plane_first_y) + " " + str(plane_last_x) + "," + str(plane_last_y) , file=sys.stderr)

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    #print("x=" + str(x) + " y=" + str(y) + " h_speed=" + str(h_speed) + " v_speed=" + str(v_speed) + " fuel=" + str(fuel) + " rotate=" + str(rotate) + " power=" + str(power), file=sys.stderr)
    h_speed_abs = abs(h_speed)
    dist_arret = h_speed_abs*(h_speed_abs+1)/2
    
    if x > plane_last_x:
        # Direction gauche
        if h_speed < 0 and x - dist_arret < plane_last_x:
            #if v_speed > -30:
            #    rotate = -90
            #if v_speed > -34:
            #    rotate = -60
            if v_speed > -37:
                rotate = -30
            else:
                rotate = -15
        elif h_speed < 0 and x - dist_arret < plane_last_x:
            rotate = -15
        elif h_speed > 0:
            rotate = 30
        else:
            rotate = 15
            
        if v_speed > 0:
            power = 3
        else:
            power = 4
            
    elif x < plane_first_x:
        # Direction droite
        if h_speed > 0 and x + dist_arret > plane_first_x:
            #if v_speed > -30:
            #    rotate = 90
            #if v_speed > -34:
            #    rotate = 60
            if v_speed > -37:
                rotate = 30
            else:
                rotate = 15
        elif h_speed > 0 and x + dist_arret > plane_first_x:
            rotate = 15
        elif h_speed < 0:
            rotate = -30
        else:
            rotate = -15
            
        if v_speed > 0:
            power = 3
        else:
            power = 4
    else:
        # On est centré
        if y + v_speed < plane_first_y:
            rotate = 0
            power = 4
        elif h_speed < 0 and x - dist_arret < plane_first_x:
            #if v_speed > -30:
            #    rotate = -90
            #if v_speed > -34:
            #    rotate = -60
            if v_speed > -37:
                rotate = -30
            else:
                rotate = -15
        elif h_speed > 0 and x + dist_arret > plane_last_x:
            #if v_speed > -30:
            #    rotate = 90
            #if v_speed > -34:
            #    rotate = 60
            if v_speed > -37:
                rotate = 30
            else:
                rotate = 15
        elif h_speed < -5:
            power = 4
            rotate = -15
        elif h_speed > 5:
            power = 4
            rotate = 15
        else:
            rotate = 0
            if v_speed > -30:
                power = 0
                rotate = 0
            elif v_speed > -34:
                power = 1
                rotate = 2
            elif v_speed > -37:
                power = 2
                rotate = 0
            elif v_speed > -38:
                power = 3
                rotate = 0
            else:
                power = 4
                rotate = 0
        
        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print(str(rotate) + " " + str(power))
