class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        global rows, cols
        rows = len(grid) 
        cols = len(grid[0])

        def dfs(grid, i, j): 
            global rows, cols
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            # base case
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0': 
                return 
            
            grid[i][j] = '0'

            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j) 
            dfs(grid, i, j + 1) 
            dfs(grid, i, j - 1)

        islands = 0
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == '1': 
                    islands += 1 
                    dfs(grid, i, j)
        return islands
            