class Solution(object):
    def countGoodStrings(self, low, high, zero, one):
        """
        :type low: int
        :type high: int
        :type zero: int
        :type one: int
        :rtype: int
        """

        dp = [0] * (high + 1)
        dp[0] = 1

        mod = 10 ** 9 + 7

        for end in range(1, high + 1): 

            if end >= zero: 
                dp[end] += dp[end - zero]
            if end >= one: 
                dp[end] += dp[end - one] 
            
            dp[end] %= mod 

        return sum(dp[low : high + 1]) % mod