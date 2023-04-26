class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        m = len(board) 
        n = len(board[0])

        if not board: 
            return False 

        def dfs(i, j, word, board):
            if len(word) == 0: 
                return True 

            if not 0 <= i < m or not 0 <= j < n:
                return False
                        
            if board[i][j] != word[0]: 
                return False
            
            temp = board[i][j]
            board[i][j] = '0'

            result = dfs(i + 1, j, word[1:], board) or \
                    dfs(i, j + 1, word[1:], board) or \
                    dfs(i - 1, j, word[1:], board) or \
                    dfs(i, j - 1, word[1:], board)
            board[i][j] = temp
            return result


        for i in range(m): 
            for j in range(n): 
                if board[i][j] == word[0]:
                    if dfs(i, j, word, board): 
                        return True
        
        return False