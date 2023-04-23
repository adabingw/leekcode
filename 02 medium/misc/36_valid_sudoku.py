class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for row in board: 
            unit = [i for i in row if i != '.']
            if len(set(unit)) != len(unit): 
                return False
        
        for col in zip(*board): 
            unit = [i for i in col if i != '.']
            if len(set(unit)) != len(unit): 
                return False

        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                unit = [m for m in square if m != '.']
                if len(set(unit)) != len(unit): 
                    return False

        return True