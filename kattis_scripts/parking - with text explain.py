t = int(input())

dict = {}
n = []
x = []

for i in range(t):
    n.insert(i, int(input()))
    x.append(list(map(int, input().split())))

x_sorted = []


for i in range(t):
    x_sorted.append(sorted(x[i]))
    x_sorted[i].append(min(x[i]))

for k in range(t):
    dist = 0
    [[dist := dist +(abs(x_sorted[k][j+1] - x_sorted[k][j]))] for j in range(len(x_sorted[k]) - 1)]
    print(dist)
