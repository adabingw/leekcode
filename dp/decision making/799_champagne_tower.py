class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [0]
        dp[0] = poured

        for i in range(1, query_row + 1):
            new_dp = [0] * (len(dp) + 1)
            new_dp[0] = max((dp[0] - 1), 0) / 2.0
            new_dp[-1] = max((dp[-1] - 1), 0) / 2.0
            for j in range(1, len(new_dp) - 1):
                new_dp[j] = max((dp[j - 1] - 1), 0) / 2.0 + max((dp[j] - 1), 0) / 2.0
            dp = new_dp

        return min(dp[query_glass], 1)
