class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Dynamic programming!!!
        #Note: Only one queen can be in a particular row and col
        Do a dynamic programming function that:
        1. At the added queen, remove all boxes that will not be possible if the queen is placed at that stack.
        """
        #mat is the entire checkerboard
        def issafe(board, row, col):
            n = len(board)

            #check the current row
            for i in range(row):
                if board[i][col]:
                    return 0
            
            #check all diagonal lefts
            i, j = row - 1, col -1
            while i >= 0 and j >= 0:
                if board[i][j]:
                    return 0
                i -= 1
                j -= 1
            
            #check all diagonal rights
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j]:
                    return 0
                i -= 1
                j += 1
            
            return 1

        def placequeens(row, board, result):
            #since nxn, use the row or col either one works just fine
            n = len(board)

            #all queens are placed
            if row == n:

                ans = []
                for i in range(n):
                    for j in range(n):
                        if board[i][j]:
                            ans.append(j+1)
                result.append(ans)
            
            for i in range(n):
                if issafe(board, row, i):
                    board[row][i] = 1
                    #continue into the next row
                    placequeens(row+1, board,result)

                    #backtrack
                    board[row][i] = 0
            
        def queensolution(n):
            board = [[0] * n for _ in range(n)]
            result = []

            placequeens(0, board, result)

            return result


        result = queensolution(n)
        print(result)
        final = []
        for i in result:
            board = [["."]*n for _ in range(n)]
            row = 0
            for j in i:
                board[row][j-1] = "Q"
                row += 1
            board = ["".join(i) for i in board]
            final.append(board)

        return final
        