class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Idea: quite a dynamic programming sort of question again
        My thought process:
        1. Count the number of numbers inside.
        2. Since three dots are ALWAYS required for an IP address. It will always be a split of 4 separate numbers.
        """
        special_characters = ['/', '@', '!', "#", "$", "%"]
        length = len(s)
        #print(length)
        res = []
        final = []
        #Even though you think you’re building a fresh list each time, reassigning back to the same variable inside the loop causes the growth. A good lesson.
        ##This is the same sort of error you see when it is about list mutations. Since lists are mutable, the variable inside the loop, since it is a list, will just grow and NOT be a separate copy. To remedy this, just add in the new combi + [i] as a new argument in the recursive function
        def backtrack(summ, combi, times):
            #root case: once the number of times (3) has been reached
            if times == 3:
                if summ > 3:
                    return
                else:
                    if summ <= 0:
                        return
                    combi = combi + [summ]
                    res.append(combi)
                    return
            
            for i in range(1,4):
                #print(combi,summ-i, time)
                backtrack(summ-i, combi + [i], times+1)

        backtrack(length, [], 0)
        print(res)

        def checkvalid(listi):
            pointer = 0
            for i in range(4):
                #print(s[pointer:pointer+listi[i]])
                if s[pointer] == "0" and listi[i] > 1:
                    return False
                if int(s[pointer:pointer+listi[i]]) > 255:
                    return False
                pointer += listi[i]
            return True

        def createIP(listi):
            IP = s
            pointer = 0
            for i in range(3):
                IP = IP[:pointer+listi[i]]+"."+ IP[pointer+listi[i]:]
                pointer += listi[i] + 1
            return IP


        for i in res:
            if checkvalid(i) == False:
                pass
            else:
                final.append(i)
        
        print(final)

        for i in range(len(final)):
            final[i] = createIP(final[i])

        return final


        