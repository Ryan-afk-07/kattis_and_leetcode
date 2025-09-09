used_words = {}
listi = []

'''

A simple readfile sort of function to remove all duplicated words with a '.'

'''

while True:
    try:
        line = input().split()
        if not line:
            break
        listi += list(line)
    except:
        break


for i in range(len(listi)):
    if listi[i].lower() in used_words.keys():
        #print('yes')
        listi[i] = '.'
    else:
        used_words[listi[i].lower()] = listi[i].lower()

print(" ".join(i for i in listi))
