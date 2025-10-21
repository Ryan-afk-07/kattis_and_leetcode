class Solution:
    def isNumber(self, s: str) -> bool:
        """
        typical dynamic programming question
        Conditions for validity:
        integer number with exponent (i.e. 19348e)
        decimal number with exponent (i.e. 23.5e93)
        """
        n = len(s)
        accept_letters = ['-', '+', '.', 'e', 'E']
        sign = ['-', '+']
        dot_ind = None
        e_ind = None
        count_sign = 0
        number_present = False
        for i in range(n):
            if s[i].isdigit() == False:
                #shit. add this in front. If the len is just one, dun care what letter it is, just return False
                if len(s) == 1:
                    return False
                #give false for all non accepted non integer chars
                if s[i] not in accept_letters:
                    print('1')
                    return False
                #check for sign. If sign is not the first val, don't bother
                if s[i] in sign and i != 0:
                    #sign cannot be last value:
                    if i == len(s)-1:
                        return False
                    #cannot have 2 signs in an integer unless it has an e before
                    if s[i-1].lower() != 'e':
                        return False
                    continue
                #check for dots and es
                if s[i] == ".":
                    #if there is already a dot, don't bother.
                    if dot_ind != None:
                        print('3')
                        return False
                    #if there is an e before this i, don't bother
                    if e_ind is not None and e_ind < i:
                        print('4')
                        return False
                    #strings with only 1 '.' is stupid
                    if len(s) == 1:
                        return False
                    #the mad mad in case the '.' is the last value and THERE IS NO NUMBER. TOTALLY NONE IN FRONT
                    if i == len(s) - 1 and number_present == False:
                        return False
                    dot_ind = i
                    continue
                if s[i].lower() == 'e':
                    #same thing as for dot. just one 'e' does not mean anything
                    if len(s) == 1:
                        return False
                    #if there is nothing before e or after e
                    if i == 0 or i == len(s)-1:
                        return False
                    #if there is already an e. There cannot be 2 es
                    if e_ind != None:
                        print('5')
                        return False
                    #if a dot is present after e
                    if dot_ind is not None and dot_ind > i:
                        print('6')
                        return False
                    #if there are NO one number before this e
                    if number_present == False:
                        return False
                    e_ind = i
                    continue
            else:
                print('7')
                number_present = True

        return True
                
        