class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Either dynamic programming using multiple scenarios of dp matrix.
        Or a combination of dp and for loops. Either one.
        Looks like a 
        """
        m = len(board)
        n = len(board[0])
        def findword(row,col, wd_ind, visited):
            #print(row, col, visited)
            #set edges to break loop and not continue with searching
            if wd_ind == len(word):
                return True
            if row < 0 or row >= m:
                return False
            if col < 0 or col >= n:
                return False
            if (row, col) in visited:
                return False
            
            if board[row][col] == word[wd_ind]:
                wd_ind += 1
                res = findword(row-1, col, wd_ind, visited + [(row, col)]) or findword(row+1, col, wd_ind, visited +[(row, col)]) or findword(row, col-1, wd_ind, visited + [(row, col)]) or findword(row, col+1, wd_ind, visited + [(row, col)])
                return res
            else:
                return False
        
        #def seeklength(row, col, max_len)
        for i in range(m):
            for j in range(n):
                """if board[i][j] == word[0]:
                    print(findword(i,j,0,[]))
                """
                if board[i][j] == word[0] and bool(findword(i,j,0,[])):
                    return True
                
                    
        return False
                        

        
            

        