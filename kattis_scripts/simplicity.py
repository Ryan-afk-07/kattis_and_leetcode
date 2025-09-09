line = input()
simpli = len(set(line))
simpli_dict = {}

for i in line:
    simpli_dict[i] = simpli_dict.get(i,0) + 1
simpli_dsort = sorted(simpli_dict.items(), key = lambda x: x[1])
#print(simpli_dsort)

def finddistinct(setty):
    if setty == 1 or setty == 2:
        return 0
    else:
        return setty - 2

def findletters(dicti, n):
    if n == 0:
        return 0
    else:
        return findletters(dicti[1:], n-1) + dicti[0][1]

if finddistinct(simpli) == 0:
    print("0")
else:
    print(findletters(simpli_dsort, finddistinct(simpli)))

'''

Question is finding the number of unique letters in a given string,
WITH EFFICIENCY

'''
    
