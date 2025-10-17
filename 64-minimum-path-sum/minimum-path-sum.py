class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        its a breadth first search or depth first search problem!
        Coupled with memoization whoop! Use breadth first. Recursive bfs
        - its taking up too much memory - need to use dynamic programming
        #set initial parameters and boundaries. List (lis) to store all eventual pathways that lead to the end.
        ## m represents row count. n represents col count.
        lis = None
        m = len(grid)
        n = len(grid[0])
        def bfs(row, col, summ):
            nonlocal lis
            #path is NOT possible
            if row >= m or col >= n:
                return
            #path is possible. Store it in the success list (lis)
            if row == m-1 and col == n-1:
                summy = summ + grid[row][col]
                liss = lis
                if lis is None or summy < liss:
                    lis = summy
                    return
                else:
                    return
            
            #create a intermediate storage sum from start to this particular 'node'
            summy = summ + grid[row][col]
            #recusive move to the next 2 cells/'nodes' - down and right. Down will be row + 1 and right will be col + 1
            down, right = bfs(row+1, col, summy), bfs(row, col+1, summy)

            return down, right
        
        bfs(0,0,0)
        return lis
        """
        m, n =  len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        #setting initial parameters for first grid cell (starting point)
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            #vertical values - since the next corner of that row can only be added with their value from the top
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for j in range(1,n):
            #for horizontal values - same reasoning as to the vertical ones
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1,m):
            for j in range(1,n):
                #this is possible because a cell can only be reached from the right or downwards. This avoids all edges. Take the smaller value between the one coming from the right and from downwards and add it with the value in that current cell.
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]
        