class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        start = [0, 0]
        directions = [
            [1, 0], [0, 1], [-1, 0], [0, -1]
        ]
        squares = 0 

        rows = len(grid) 
        cols = len(grid[0])

        global paths
        paths = 0

        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 1: 
                    start[0] = i 
                    start[1] = j 
                if grid[i][j] == 0: 
                    squares += 1

        def dfs(row, col, squares_walked): 
            global paths
            if grid[row][col] == 2: 
                if squares_walked - 1 == squares: # minus one cuz we also count the ending square as a step
                    paths += 1
                return 
            
            if grid[row][col] == -1 or grid[row][col] == -2: 
                return 

            # marked as read
            grid[row][col] = -2

            for direction in directions: 
                i = row + direction[0]
                j = col + direction[1] 
                if 0 <= i < rows and 0 <= j < cols: 
                    dfs(i, j, squares_walked + 1) 
            
            # restore steps
            grid[row][col] = 0
        
        dfs(start[0], start[1], 0) 
        return paths 
