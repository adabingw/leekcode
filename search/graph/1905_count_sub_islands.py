class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        
        global rows, cols, islands, result
        islands = 0
        result = 0
        rows = len(grid2) 
        cols = len(grid2[0])

        def dfs(grid, i, j): 
            global rows, cols, islands, result
            
            # base case
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0: 
                return

            if grid[i][j] == 1 and grid1[i][j] == 0:
                islands -= 1
            
            grid[i][j] = 0

            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j) 
            dfs(grid, i, j + 1) 
            dfs(grid, i, j - 1)

        for i in range(rows): 
            for j in range(cols): 
                if grid2[i][j] == 1 and grid1[i][j] == 1: 
                    islands = 1
                    dfs(grid2, i, j)
                    if islands > 0:
                        result += 1
        return result