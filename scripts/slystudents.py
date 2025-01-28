from math import *

line = map(str, input().split())

'''
below solve function is to do the gcd calculation for a letter or multiple letters
It may most likely be based off from a tutorial on gcd and ASCII
'''
def solve(nums):
    if len(nums) == 1:
        return nums[0]
    div = gcd(nums[0], nums[1])

    if len(nums) == 2:
        return div

    for i in range(1, len(nums) - 1):
       div = gcd(div, nums[i + 1])
       if div == 1:
           return div
    return div
    

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        print(n)
        n, r = divmod(n, 3)
        nums.append(str(r))
    return int(''.join(reversed(nums)))

for i in line:
    ASCII = []
    for j in i:
        ASCII.append(ord(j))
    
    factor = solve(ASCII)
    ASCII_red = [k//factor for k in ASCII]
    Base3 = [str(ternary(m)) for m in ASCII_red]
    print(factor)
    print(" ".join(Base3))
    
