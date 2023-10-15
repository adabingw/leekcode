class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        def dfs(row, col):
            # base case
            if not (0 <= row < rows and 0 <= col < cols) or grid[row][col] < 1:
                return 0

            res = grid[row][col]
            grid[row][col] = -1

            res += dfs(row + 1, col)
            res += dfs(row - 1, col)
            res += dfs(row, col + 1)
            res += dfs(row, col - 1)
            return res

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    result = max(result, dfs(i, j))
        
        return result
