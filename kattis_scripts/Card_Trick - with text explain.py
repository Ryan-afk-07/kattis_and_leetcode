test_cases = int(input())

#def countzero(zero, q,o,p, result):
#    while zero < q:
#        for k in list(range(o, p)) + list(range(0, o)):
#            if permu[k] == 0 and zero < q:
#                zero += 1
#                result += 1
#            elif zero < q:
#                result += 1
#            else:
#                break
#    print(j, zero, result)
#    return j, zero, result


for i in range(test_cases):
    n = int(input())
    permu = [0]*n
    cards = n
    for j in range(1, n+1):
        #first case - first card will always be the second from top
        if j == 1 and cards > 1:
            permu[j] = j
        #second case - setting the second card
        elif sum(range(2,(j+2))) <= n:
            permu[sum(range(2,(j+2))) - 1] = j
        #third case - setting the third card
        elif sum(range(2, (j+2))) == n + 1:
            permu[0] = j
        #fourth case - looping the number of zeros for the remaining numbers, such that the next card will be set at the zero-ed place after going through the set number of zeros (i.e. cards)
        elif j <= n:
            zero = 0
            result = 0
            while zero < j+1:
                for k in list(range(permu.index(j-1), n)) + list(range(0, permu.index(j-1))):
                    if permu[k] == 0 and zero < j+1:
                        zero += 1
                        result += 1
                    elif zero < j+1:
                        result += 1
                    else:
                        break
            #countzero(zero, (j+1), permu.index(j-1), n, result)
            permu[(permu.index(j-1) +(result)-1)%n] = j
        else:
            break

    print(*permu)
