# First 'import PIVolumeLib as PVL' *MAKE SURE THIS FILE IS IN THE ROOT DIRECTORY OF YOUR MAIN.py PROJECT.*
# then you can do "PVL." then whatever function you want to execute.

import math

PI = 3.141592654

# -- Cube --
def cubevol(L, W, H):
    A = L * W * H
    return A

# -- TRIANGLE --
def triarea(base, height, rounding):
    A = 0.5 * (base * height)
    if rounding == True:
        return round(A)
    else:
        return A
    
# -- parallelogram --
def paraarea(base, height, rounding):
    A = base * height
    if rounding == True:
        return round(A)
    else:
        return A

# -- Trapezoid --
def traparea(height, baseone, basetwo, rounding):
    A = 0.5 * height * (baseone + basetwo)
    if rounding == True:
        return round(A)
    else:
        return A

# -- Circle --    
def circlearea(radius, rounding):
    A = PI * math.pow(radius, 2)
    if rounding == True:
        return round(A)
    else:
        return A
    
# -- Hemisphere
def hemivol(radius, rounding):
    V = 0.5 * 1.3333 * PI * math.pow(radius, 2)
    if rounding == True:
        return round(V)
    else:
        return V

# -- Cylinder --    
def rightcyl(radius, height, rounding):
    V = (PI * math.pow(radius, 2)) * height
    if rounding == True:
        return round(V)
    else:
        return V

# -- Cone --    
def rightcone(radius, height, rounding):
    V = (0.3333 * PI * math.pow(radius, 2)) * height
    if rounding == True:
        return round(V)
    else:
        return V

# -- Sphere --
def spherevol(radius, rounding):
    V = 1.3333 * PI * math.pow(radius, 3)
    if rounding == True:
        return round(V)
    else:
        return V

# -- Pythagorean Theorem --   
def pyth(A, B, rounding):
    ct = math.pow(A, 2) + math.pow(B, 2)
    C = math.sqrt(ct)
    if rounding == True:
        return round(C)
    else:
        return C
    
# -- square/rectangle --
def square_rectarea(L, H):
    A = L * H
    return A
