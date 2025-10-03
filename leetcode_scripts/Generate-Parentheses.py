class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        """
        Idea: do as what a normal permutation will do. Just keep the edges as they are and move the rest around. Use the backtrack mechanism
        
        if n == 1:
            return ["()"]
        lis = (["("] * n) + ([")"] * n)
        lis_index = list(range(1, n*2 -1))
        print(lis, lis_index) 
        exists = []
        def backtrack(ind, numm, combi):
            if numm == []:
                return
            while ind < len(numm):
                nummy = numm
                backtrack(ind +1, nummy, combi)
                combi = combi + [nummy[ind]]
                nummy = numm[:ind] + numm[ind+1:]
                backtrack(0, nummy, combi)
                if len(combi) == len(lis_index) and combi not in exists:
                    final.append(combi)
                    exists.append(combi)
                    break
                else:
                    break
        
        final = []
        backtrack(0, lis_index, [])
        finaly = []
        for i in final:
            temp = ["("] + [lis[num] for num in i] + [")"]
            temp_string = "".join(temp)
            if temp_string in finaly:
                continue
            else:
                finaly.append(temp_string)
        
        print(finaly)


        return

        """

        """
        Idea 2: do a combination sum instead. Then do the parentheses allocation based on combi
        Does not work because it MUST be parentheses.
        """
        #how the combinations work is for the range of numbers below n, do a recursive finding of each combination prior before addition of this particular number
        """
        eg. For i == 1
        findCombinations will be findCombinations(2) which will move to this command that will require findCombinations(1), this will be done until base case result is retrieved (i.e. findCombinations(0) == [[]])
        for tail in findCombinations that tail argument is taking results for each number below n that is calculated
        Hence only when findCombinations(0) returns a result, then the [i] + tail will work for subsequent findCombinations. I.e. findCombinations(1) will end with [[1]] then findCombinations will end with [[1,1]] because tail is found for the previous iteration
        
        def findCombinations(n):
            if n == 0:
                return [[]]
            
            result = []
            for i in range(1, n+1):
                for tail in findCombinations(n-i):
                    #print(i, result, tail)
                    result.append([i] + tail)
            return result 

        if n == 1:
            return ["()"]
        
        combi = findCombinations(n)
        final = []
        for i in combi:
            res = ["("*num + ")"*num for num in i]
            final.append("".join(res))

        print(final)
        """

        """
        Seen idea: depth first search.
        """
        res = []
        def dfs(openP, closeP, s):
            #base case - when open parentheses and closed parentheses are formed (i.e. parentheses closed successfully) and max number of parentheses used
            if openP == closeP and openP + closeP == n * 2:
                res.append(s)
                return
            
            #parentheses is closed but there are not yet n parentheses formed
            if openP < n:
                #print(openP, closeP, res, "hi1")
                dfs(openP + 1, closeP, s + "(")
            
            #case if parentheses is still open. lacks a closure
            ##this line is important because it allows for opportunities where openP == n - 1/n-2 etc and closeP < openP situations to happen since this line will take in those situations as well. Making more patterns doable.
            if closeP < openP:
                #print(openP, closeP, res, "hi2")
                dfs(openP, closeP + 1, s+")")

        dfs(0,0,"")

        return res