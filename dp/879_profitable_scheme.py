class Solution(object):
    def profitableSchemes(self, n, minProfit, groups, profits):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        dp = [[0] * (n + 1) for i in range(minProfit + 1)]
        dp[0][0] = 1

        for profit, group in zip(profits, groups):
            for i in range(minProfit, -1, -1):
                for j in range(n - group, -1, -1):
                    dp[min(i + profit, minProfit)][j + group] += dp[i][j]

        return sum(dp[minProfit]) % (10**9 + 7)
