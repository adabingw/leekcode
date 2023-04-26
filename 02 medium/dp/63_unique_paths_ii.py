class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(grid) 
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)] 

        dp[0][0] = 1 if grid[0][0] == 0 else 0

        for i in range(1, m): 
            if grid[i][0] != 1:
                dp[i][0] = dp[i - 1][0]
        
        for i in range(1, n): 
            if grid[0][i] != 1:
                dp[0][i] = dp[0][i - 1]

        for i in range(1, m): 
            for j in range(1, n): 
                if grid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]