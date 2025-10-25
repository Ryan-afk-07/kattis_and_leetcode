class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Idea: pointer.
        1. if we touch a non integer string, immediately end the movement
        2. First char, if not an integer, can only be a sign. If not, end movmement. Have a sign variable as well in case its a negative.
        3. Whitespaces are ignored, so if chance upon that, move along.
        """
        integers_spec = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        integers_dic = {
            '1':1,'2':2,'3':3,
            '4':4,'5':5,'6':6,
            '7':7, '8':8, '9':9,
            '0':0 
        }
        sign = "+"
        has_sign = False
        has_zeros = False
        sliced = ""
        maxnegvalue = '8463847412'
        maxvalue = '7463847412'
        #maybe i do the snipping of trailing zeros, whitespaces and signs at the front first
        while len(s) >= 1 and s[0] in ['0', ' ', '+', '-']:
            if has_zeros == False and has_sign == False:
                if s[0] == "0":
                    has_zeros = True
                    s = s[1:]
                elif s[0] == "+":
                    has_sign = True
                    s = s[1:]
                elif s[0] == "-":
                    sign = "-"
                    has_sign = True
                    s = s[1:]
                else:
                    s = s[1:]
            else:
                if s[0] in ["+", "-", ' ']:
                    return 0
                else:
                    s = s[1:]
        
        print(s)
        if not s:
            return 0
        pointer = 0
        while pointer < len(s):
            print(pointer, sliced, len(s))
            #immediately analyze string if it is already at 10 length (which is the amnt of chars for 2**31)
            if len(sliced) > 10:
                if sign == "-":
                    return -2**31
                else:
                    return 2**31 - 1
            if len(sliced) == 10:
                if sign == "-":
                    for i in range(len(sliced)-1,-1,-1):
                        if integers_dic[sliced[i]] == integers_dic[maxnegvalue[i]]:
                            pass
                        elif integers_dic[sliced[i]] > integers_dic[maxnegvalue[i]]:
                            return -2**31
                        else:
                            break
                else:
                    for i in range(len(sliced)-1,-1,-1):
                        if integers_dic[sliced[i]] == integers_dic[maxvalue[i]]:
                            pass
                        elif integers_dic[sliced[i]] > integers_dic[maxvalue[i]]:
                            return 2**31 - 1
                        else:
                            break
                    
            ##print(s[pointer])
            #takes care of any non integer that appears after a legitimate integer
            if s[pointer] not in integers_spec:
                break
            else:
                sliced = s[pointer] + sliced
                pointer += 1
    
        res = 0
        print(sliced)
        #in case of situations where there is a bloody +- joke
        if not sliced:
            return 0
        #in case tester fools me with 11 char string that has furst 10 char lesser than 2**31 - 1
        if len(sliced) > 10:
            if sign == '-':
                return -2**31
            else:
                return 2**31 - 1
        #fuck sake: place this in case the strings are EXACTLY the same
        if sliced == maxvalue and sign == "+":
            return 2**31 - 1
        if sliced == maxnegvalue and sign == "-":
            return -2**31

        if len(sliced) == 10 and sign == "-":
            for i in range(len(sliced)-1,-1,-1):
                if integers_dic[sliced[i]] == integers_dic[maxnegvalue[i]]:
                    pass
                elif integers_dic[sliced[i]] > integers_dic[maxnegvalue[i]]:
                    return -2**31
                else:
                    for i in range(len(sliced)):
                        print(res)
                        res += integers_dic[sliced[i]] * (10**i)
                    return -res
                
        elif len(sliced) == 10 and sign == "+":
            for i in range(len(sliced)-1,-1,-1):
                if integers_dic[sliced[i]] == integers_dic[maxvalue[i]]:
                    pass
                elif integers_dic[sliced[i]] > integers_dic[maxvalue[i]]:
                    return 2**31 - 1
                else:
                    for i in range(len(sliced)):
                        print(res)
                        res += integers_dic[sliced[i]] * (10**i)
                    return res
        else:
            print('heckyea')
            for i in range(len(sliced)):
                print(res)
                res += integers_dic[sliced[i]] * (10**i)
            if sign == '-':
                return -res
            else:
                return res

            
                
        #if string is lesser than 10 or equals to 10 but is still lesser than 2**31 - 1
         
        


