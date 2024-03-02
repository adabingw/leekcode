class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        result = len(prices)
        dp = [0] * len(prices)

        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                dp[i] = dp[i - 1] + 1
        
        result += sum(dp)
        return result