class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board 
        self.solve()
    
    def solve(self): 
        row, col = self.find_unassigned() 
        if [row, col] == [-1, -1]: 
            return True

        for num in range(1, 10): 
            if self.safe(row, col, str(num)): 
                self.board[row][col] = str(num) 
                if self.solve(): 
                    return True 
                self.board[row][col] = '.'
        return False

    def find_unassigned(self): 
        for row in range(9): 
            for col in range(9): 
                if self.board[row][col] == '.': 
                    return row, col
        return -1, -1

    def safe(self, row, col, cell): 
        square_row = row - row % 3
        square_col = col - col % 3 

        for c in range(9): 
            if self.board[row][c] == cell: 
                return False 
        
        for r in range(9): 
            if self.board[r][col] == cell: 
                return False 

        for r in range(square_row, square_row + 3): 
            for c in range(square_col, square_col + 3): 
                if self.board[r][c] == cell: 
                    return False 
        
        return True 
