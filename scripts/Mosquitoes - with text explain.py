M = []
P = []
L = []
E = []
R = []
S = []
N = []

def appendix(m,n):
    m.append(int(n))

while True:
    line = input().split()
    if line:
        appendix(M, line[0])
        appendix(P, line[1])
        appendix(L, line[2])
        appendix(E, line[3])
        appendix(R, line[4])
        appendix(S, line[5])
        appendix(N, line[6])
    else:
        break

#setting algorithm for each weeks number of larva, pupa and mosquitoes - based on how many will die, and how many will grow etc
for i in range(len(N)):
    larva = [0]*(N[i]+1)
    pupa = [0]*(N[i]+1)
    mosqui = [0]*(N[i]+1)
    eggs = E[i]
    larvagrow = R[i]
    pupagrow = S[i]
    for j in range(0, N[i]+1):
        if j == 0:
            mosqui[j] = M[i]
            larva[j] = L[i]
            pupa[j] = P[i]
        else:
            larva[j] = (mosqui[j-1]*eggs)
            pupa[j] = (larva[j-1]//larvagrow)
            mosqui[j] = (pupa[j-1]//pupagrow)
    print(mosqui[-1])



