line = input().split()
height = int(line[0])
root = 0
for i in range(height + 1):
    root += 2**i

ans = root
incre = 0
#placing algorithm to note the pattern.
#left movement will start from 1 and right movement will start from 2
if len(line) == 1:
    print(ans)
else:
    decision = list(line[1][:])
    #print(decision[0], decision[1])
    if decision[0] == "L":
        incre = 1
        ans = ans - incre
        for i in range(len(decision) -1):
            if decision[i] == "L" and decision[i+1] == "L":
                incre = 2 * incre
                ans = ans - incre
            elif decision[i] == "L" and decision[i+1] == "R":
                incre = (2* incre) + 1
                ans = ans - incre
            elif decision[i] == "R" and decision[i+1] == "L":
                incre = (2*incre) - 1
                ans = ans - incre
            elif decision[i] == "R" and decision[i+1] == "R":
                incre = (2*incre)
                ans = ans - incre
            else:
                break
    elif decision[0] == "R":
        incre = 2
        ans = ans - incre
        for i in range(len(decision) - 1):
            if decision[i] == "L" and decision[i+1] == "L":
                incre = 2 * incre
                ans = ans - incre
            elif decision[i] == "L" and decision[i+1] == "R":
                incre = (2* incre) + 1
                ans = ans - incre
            elif decision[i] == "R" and decision[i+1] == "L":
                incre = (2*incre) - 1
                ans = ans - incre
            elif decision[i] == "R" and decision[i+1] == "R":
                incre = (2*incre)
                ans = ans - incre
            else:
                break

    print(ans)
                
