class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)
        grid2 = [[0] * n for _ in range(n)]

        for i, row in enumerate(grid):
            max_height = max(row)
            for j, cell in enumerate(row):
                grid2[i][j] = max_height

        for j, col in enumerate(grid[0]):
            max_height = 0
            max_height_changed = 0
            for i, row in enumerate(grid):
                max_height = max(max_height, grid[i][j])
                max_height_changed = max(max_height_changed, grid2[i][j])
            
            if max_height_changed > max_height:            
                for i, row in enumerate(grid):
                    if grid2[i][j] > max_height:
                        grid2[i][j] = max_height
            
        result = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(grid):
                result += grid2[i][j] - grid[i][j]

        return result
