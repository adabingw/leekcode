class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        dp = [triangle[0]]

        for i in range(1, len(triangle)):
            dp.append([ float('inf') for _ in range(len(triangle[i]))])
            for j, v in enumerate(triangle[i]):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = triangle[i][j] + dp[i - 1][-1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])
        return min(dp[-1])