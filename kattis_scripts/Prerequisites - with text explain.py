


while True:
    try:
        
        line = input().split()
        if len(line) == 2:
            freddie = []
            modules = []
            modules_no = []
            passes = []
            n = list(map(int, input().split()))
            freddie.append(n)
            for i in range(int(line[1])):
                n = list(map(int, input().split()))
                modules_no.append(n[1])
                modules.append(n[2:])
            #check if freddie's modules is in the list of categories modules
            #each fit adds counter to check that freddie did take the min no. of mods in that cat
            for i in range(len(freddie)):
                for j in range(len(modules)):
                    count = 0
                    for k in range(len(freddie[i])):
                        if freddie[i][k] in modules[j]:
                            count = count + 1
                        else:
                            pass
                    passes.append(count)
                x = ['satisfied' if passes[i] >= modules_no[i] else 'not satisfied' for i in range(len(modules))]
                if "not satisfied" in x:
                    print("no")
                else:
                    print("yes")
        elif len(line) == 1:
            break
        else:
            pass
    except:
        break

            
