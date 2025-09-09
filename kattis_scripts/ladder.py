import math

'''

calculate ladder parameters i presume

'''

h, v = map(int, input().split())


ladder = h/math.sin(math.radians(v))

print(math.ceil(ladder))
