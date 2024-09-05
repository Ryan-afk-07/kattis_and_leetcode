def compositions(n,m,k,mem):
    if (n,m,k) not in mem:
        if n==0:
            return 1
        s = 0
        for i in range(n,0,-1):
            if i % k != m:
                print(s)
                s += compositions(n-i,m,k,mem)
                print(s)
        print(mem.items())
        mem[(n,m,k)] = s
    return mem[(n,m,k)]


#def main():
#    mem = {}
#    for _ in range(int(input())):
#        case, n, m, k = map(int,input().split())
#        print(f'{case} {compositions(n,m,k,mem)}')

n = int(input())
mem = {}
for i in range(n):
    line = input().split()
    set_no = int(line[1])
    m = int(line[2])
    k = int(line[3])
    compositions(set_no, m,k, mem)
    break


