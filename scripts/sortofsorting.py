while True:
    n = int(input())
    W = []
    if n:
        #this is simply doing a bubble sort or something haha
        for _ in range(n):
            W.append(input())
        for i in range(len(W) - 1):
            for j in range(len(W)-i-1):
                if W[j][0:2]> W[j+1][0:2]:
                    W[j],W[j+1]=W[j+1],W[j]
        for i in W:
            print(i)
        print(" ")
    else:
        break
            
            
