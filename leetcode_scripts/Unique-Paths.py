class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        This is a typical bfs or dfs. Need to learn its mechanism.
        Need to force myself to learn its algorithm
        """
        memo = {}
        def dfs(row, col):
            #first case: if algorithm has reached past boundaries
            if row >= m or col >= n:
                return 0
            #success case: when the algorithm has reached the right end
            if row == m-1 and col == n-1:
                return 1
            
            if (row, col) in memo:
                return memo[(row, col)]

            # Recursive step: Explore paths by moving down and right
        # The total unique paths from (row, col) is the sum of paths from (row+1, col) and (row, col+1)
            paths_from_current = dfs(row+1, col) + dfs(row, col+1)

            memo[(row,col)] = paths_from_current
            return paths_from_current
        
        return dfs(0,0)
        