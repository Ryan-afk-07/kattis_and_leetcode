counter = 0
def printDay(counter):
    print ("Day " + str(counter))

def calcprice(dic):
    for values in dic.keys():
        #this is because the values of the primary dictionary is ANOTHER created dict
        calc = []
        for key, value in dic[values].items():
            #doing calculation of duration for the person on that day
            duration = []
            for i in value:
                duration.append(i)
            calc.append(duration)
        print(calc)
        fee = []
        #because the duration values taken are in a list again, need to deep search twice
        for i in range(len(calc)-1):
            for j in range(len(calc[i])):
                fee.append(calc[i+1][j] - calc[i][j])
        print(fee)
        print("$" + "" + str(format(sum(fee) * 0.10, '.2f')))
            

while True:
    n = input()
    if str(n) == "OPEN":
        #print day command is just to visualize the day 1 and day 2 stuff only
        printDay(counter+1)
        counter += 1
        customers = {}
        while True:
            line = input().split()
            if len(line) != 1:
                #essentially means if the 'CLOSE' command isn't present
                name = str(line[1])
                status = str(line[0])
                dur = int(line[2])
                ''' below are the commands to input the entry and exit times in dictionary '''
                if status == "ENTER" and name not in customers.keys():
                    customers[name] = {}
                    customers[name][status] = []
                    customers[name][status].append(dur)
                elif status == "EXIT" and status not in customers[name]:
                    customers[name][status] = []
                    customers[name][status].append(dur)
                elif status == "ENTER":
                    customers[name][status].append(dur)
                elif status == "EXIT":
                    customers[name][status].append(dur)
                else:
                    pass
            else:
                myKeys = list(customers.keys())
                myKeys.sort()
                sorted_cust = {i: customers[i] for i in myKeys}
                print(sorted_cust.items())
                calcprice(sorted_cust)
                break
        else:
            pass

