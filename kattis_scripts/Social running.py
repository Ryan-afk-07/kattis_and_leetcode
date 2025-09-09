n = int(input())
distances = []
for i in range(n):
    dist = int(input())
    distances.append(dist)

alone_dist = []

for i in range(len(distances)):
    #finding the distances each person has to run if it started with a specific person from a list
    alone_dist.append(distances[i%n]+distances[(i-2)%n])

print(min(alone_dist))
    
