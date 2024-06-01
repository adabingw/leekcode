class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """

        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        grid = [ [''] * n for _ in range(m) ]

        for i, j in walls:
            grid[i][j] = 'W'
        
        for i, j in guards:
            grid[i][j] = 'G'
        
        def markGrid(i, j, dir):
            if not (0 <= i < m) or not (0 <= j < n):
                return
            if grid[i][j] == 'W' or grid[i][j] == 'G':
                return

            grid[i][j] = '-'
            
            markGrid(i + dir[0], j + dir[1], dir)
        
        for i, j in guards:
            for x, y in direction:
                markGrid(i + x, j + y, [x, y])
        
        result = 0

        for i in range(m):
            for j in range(n):
                result = result + 1 if grid[i][j] == '' else result

        return result