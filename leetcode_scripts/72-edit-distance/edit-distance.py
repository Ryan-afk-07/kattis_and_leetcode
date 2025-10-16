class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """ 
        Can't understand how to tackle this question. So referred to solution.
        Solution showed 3 essential actions: insert, delete and replace.
        Set dynamic programming for insert, delete and replace.
        """
        #function dp(i,j) = min no. of operations needed to convert 1st i chars of word1 to first j chars of word2
        #delete word: dp(i,j) = 1 + dp(i-1, j) - why = goal is to edit word1 to word2, so eventual result is i-1
        #insert word: dp(i,j) = 1 + dp(i, j-1) essential making word1 add a necessary letter that is in word2, so in technicality, just remove that letter to be added in word2
        #replace word - needs to be split into 2 scenarios
        #scenario 1, characters diff: replacement counts as an action: dp(i,j) = 1 + dp(i-1, j-1)
        #scenario2, characters are eq: replacement DOES not count as an action: dp(i,j) = dp(i-1, j-1)
        #of course the base cases: dp(0,j) = j, dp(i,0) = i

        #memoization dict
        cache = {}

        def dp(i,j):
            if (i,j) in cache:
                #purely to save computing power by memoization
                return cache[(i,j)]
            
            #i believe they are the base cases. if one str is null and another is of a certain length. Then obviously you would need the number of actions in the char which still has that no of letters. 
            if i == 0:
                return j
            if j == 0:
                return i
            
            #replacement that does not count as 
            if word1[i-1] == word2[j-1]:
                res = dp(i-1, j-1)
            else:
                #take the minimum number of actions needed duh
                res = 1 + min(
                    dp(i-1,j),
                    dp(i,j-1),
                    dp(i-1,j-1)
                )
            
            cache[(i,j)] = res
            return res
        
        return dp(len(word1), len(word2))
        