class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(board, i, j): 
            global rows, cols 
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] == 'X' or board[i][j] == '-': 
                return  

            board[i][j] = '-'

            dfs(board, i + 1, j) 
            dfs(board, i - 1, j) 
            dfs(board, i, j + 1) 
            dfs(board, i, j - 1)
            return 
            
        if len(board) == 0: return None  

        global rows, cols 
        rows = len(board) 
        cols = len(board[0])

        for i in range(rows): 
            for j in range(cols): 
                if board[i][j] == 'O' and (i == 0 or i == rows - 1 or j == 0 or j == cols - 1): 
                    dfs(board, i, j)
        
        for i in range(rows): 
            for j in range(cols): 
                if board[i][j] == '-': board[i][j] = 'O'
                elif board[i][j] == 'O': board[i][j] = 'X'

        return