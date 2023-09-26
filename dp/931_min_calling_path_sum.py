class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        dp = [[0] * n for _ in range(n)]

        dp[0] = matrix[0]

        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + matrix[i][0]
            dp[i][-1] = min(dp[i - 1][-1], dp[i - 1][-2]) + matrix[i][-1]
            for j in range(1, n - 1):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
            
        return min(dp[-1])
