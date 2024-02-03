class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        global area, n, m
        n = len(grid)
        m = len(grid[0])
        result = 0
        area = 0

        def dfs(i, j):
            global area, n, m
            area += 1
            grid[i][j] = 0
            for x, y in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                new_i, new_j = i + x, j + y
                if (new_i >= 0 and new_i < n and new_j >= 0 and new_j < m):
                    if (grid[new_i][new_j] == 1):
                        dfs(new_i, new_j)
            return
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i, j)
                    result = max(result, area)
                    area = 0
        
        return result
