class Solution(object):
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])
        
        result = 0
        directions = [[-1, 1], [0, 1], [1, 1]]

        def dfs(i, j):
            res = 0
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < m and 0 <= new_j < n:
                    if grid[new_i][new_j] > grid[i][j]:
                        res = max(dfs(new_i, new_j), res)
            grid[i][j] = float('inf')
            return res + 1

        for k in range(m):
            result = max(result, dfs(k, 0))
        return result - 1
