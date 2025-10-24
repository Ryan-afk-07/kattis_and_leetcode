class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Dynamic programming?
        Do a move through the entire dataset, to check the row, col space where all the 0s are and thereafter do the necessary conversion
        """
        '''
        row_zero = []
        col_zero = []
        #print(len(matrix), len(matrix[0]))
        def move_across(row,col):
            if row >= len(matrix) or col >= len(matrix[0]):
                return
            if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
                if matrix[row][col] == 0:
                    if row not in row_zero:
                        row_zero.append(row)
                    if col not in col_zero:
                        col_zero.append(col)
                    return
                return
            #print(row, col)
            if matrix[row][col] == 0:
                if row not in row_zero:
                    row_zero.append(row)
                if col not in col_zero:
                    col_zero.append(col)
            
            down, right = move_across(row+1, col), move_across(row, col+1)
            return down, right


        
        move_across(0,0)

        for i in range(len(matrix)):
            if i in row_zero:
                matrix[i] = [0] * len(matrix[0])
                continue
            for j in col_zero:
                matrix[i][j] = 0
        
        print(row_zero, col_zero)
        #print(matrix)
        '''
        """
        My idea not time efficient enough. Works but not efficient.
        Saw solution: better idea.
        Check if first row and first col has zeros (cos if they have, the whole col and row line will be zero-fied.). Save boolean values for them
        For the rest of the columns, check if the value is zero. If it is, change the first values of that row and col to 0. since that whole row or col will have to be zero.
        Then do the conversion for the non-first row/first col ones first
        Afterwhich, end with the first row and col conversion
        """
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        #setup where first row has a zero
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True
                break
        #setup where first col has a zero
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
                break
        
        #do investigation for all other rows and cols
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        #change all values in that row in which that indexed first value of the row is a 0
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0
        
        #change all values in that column in which that indexed first value of the column is a 0
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
        

        if first_row_zero == True:
            for c in range(cols):
                matrix[0][c] = 0
        
        if first_col_zero == True:
            for r in range(rows):
                matrix[r][0] = 0


        return matrix
        