class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Solution mentions the use of DP and recursion.

        """
        if len(s1) + len(s2) != len(s3):
            return False
        
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i == len(s1) and j == len(s2):
                return True
            choose_s1, choose_s2 = False, False
            if i < len(s1) and s1[i] == s3[i+j]:
                choose_s1 = dfs(i+1, j)
                cache[(i+1, j)] = choose_s1
            if j < len(s2) and s2[j] == s3[i+j]:
                choose_s2 = dfs(i, j+1)
                cache[(i, j+1)] = choose_s2
            
            #putting choose_s1 and choose_s2 as False is to prevent that value from being taken. How smart.
            return choose_s1 or choose_s2
        
        return dfs(0,0)
            
            


        

        

        