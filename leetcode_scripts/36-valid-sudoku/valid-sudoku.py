class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Essential idea behind this analysis:
        1. If a number of a cell is seen in its row or its column, straight away return False
        2. If a number of a cell is seen in its 3x3 cube around it. return False.
        3. Move throughout the whole 9x9. If there is no 1 nor 2 over the whole 81 cells, return True
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r//3, c//3)]:
                    return False

                #add cell to the row key the cell is in
                rows[r].add(board[r][c])
                #add cell to the col key the cell is in
                cols[c].add(board[r][c])
                #add cell to the 3x3 box the cell is in
                #why //3 is just because the whole sudoku is 9x9. You //3 to get each 3x3 box the cell is in
                boxes[(r//3, c//3)].add(board[r][c])
        
        print(rows, cols, boxes)
        return True
        