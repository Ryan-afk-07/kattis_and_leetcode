import sys

input = sys.stdin.readline
n,k = map(int, input().split())
a_string = list(input().split())

a = []

for i in a_string:
    a.append(int(i))

if k == a[0]:
    print("fyrst")
elif k == a[1]:
    print("naestfyrst")
else:
    print(str(a.index(k) + 1) + " " + "fyrst")

print(a)

'''essentially an easy question to find out the position of a letter in a string'''
