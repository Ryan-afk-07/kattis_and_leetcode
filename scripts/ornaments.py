from math import *

while True:
    try:
        line = list(map(int, input().split()))
        if line != [0, 0, 0]:
            r, h, s = line[0], line[1], (line[2])
            #print(s)
            arc = (2*pi - 2*(acos(r/h))) * r
            diag = 2* (((h**2) - (r**2))**0.5)
            length = (arc + diag) * (1 + s/100)
            print(format(round(length, 2), '.2f'))
        else:
            break
    except:
        break

'''

Simple calculation of ornament circumference or something.
Simple math stuffs - just need to understand the design of the ornament

'''
