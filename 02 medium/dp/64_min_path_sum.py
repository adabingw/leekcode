class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid) 
        n = len(grid[0]) 

        dp = [[0] * n for i in range(m)]
        dp[0][0] = grid[0][0]

        # first row 
        for i in range(1, n): 
            dp[0][i] = dp[0][i - 1] + grid[0][i] 
        
        # first col 
        for j in range(1, m): 
            dp[j][0] = dp[j - 1][0] + grid[j][0] 

        for i in range(1, m): 
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]