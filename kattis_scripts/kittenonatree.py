'''

Question requires us to find the back path of a branch that a kitten is on
Idea is to create a dictionary where a root has these branches, and do some backtrack in finding the keys from its values

'''



kitten_spot = int(input())
tree = {}
while True:
    try:
        inp = input()
        if inp != '-1':
            lis = list(map(int, inp.split()))
            tree[lis[0]] = lis[1:]
        else:
            break
    except:
        break

path = []

def backtrack(branch, dicti, lis):
    #creating a key for each branch (branched values are dict values for that key)
    back = [key for key in dicti.keys() if branch in dicti[key]]
    if len(back) == 0:
        return
    else:
        #essentially assuming that each branch links to unique values, add the root into the result list and do the same
        #recursive function on that root until that root has no value (in this case it will be the ground/main root)
        track = back[0]
        lis.append(track)
        backtrack(track, dicti, lis)
        
    

backtrack(kitten_spot, tree, path)
path = [kitten_spot] + path

for i in path:
    print(i, end = " ")
        
