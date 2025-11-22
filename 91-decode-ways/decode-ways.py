class Solution:
    def numDecodings(self, s: str) -> int:
        """
        the below function shows memoization and dynamic programming. I.e. using stored previous values as a reference to the next. Its a rather similar technique as to the number of paths from a certain start to end. Same as the n-queens question. All dynamic programming.
        """
        
        if not s or s[0] == "0":
            return 0

        end = len(s)
        memo = {}

        def dfs(start):
            if start == end:
                return 1  # one valid decode path
        
            if start in memo:
                return memo[start]
        
            if s[start] == "0":
                return 0  # can't decode starting with 0
        
            ways = dfs(start + 1)  # take 1 digit
        
            # take 2 digits only if it's valid (<= 26)
            if start + 1 < end and int(s[start:start+2]) <= 26:
                ways += dfs(start + 2)
        
            memo[start] = ways
            return ways
        return dfs(0)
