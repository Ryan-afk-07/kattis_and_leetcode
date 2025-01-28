from math import *

line = input().split()
k,w,l = int(line[0]), int(line[1]), int(line[2])

def multiplier(n):
    start = 1
    for i in range(1, n+1):
        if i == n:
            start = start + 2**(i)
        else:
            start = start + 2**(i+1)
    return start

length = l/multiplier(k)
#print(multiplier(k))
print(atan(2*length/w)*180/pi)

'''

Question requests us to calculate the initial angle of throw such that:
1. the ball bounces off the wall at a specified number of times
2. the ball accurately reaches the middle of the whole lane at its last bounce

'''
