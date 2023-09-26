class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        result = 0
        
        for i in range(m):
            result = max(result, int(matrix[0][i]))
            dp[0][i] = int(matrix[0][i])
        for i in range(n):
            result = max(result, int(matrix[i][0]))
            dp[i][0] = int(matrix[i][0])

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    result = max(result, dp[i][j])
        
        return result ** 2
