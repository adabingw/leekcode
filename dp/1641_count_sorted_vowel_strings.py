class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1, 1, 1, 1]
        for i in range(1, n):
            for j in xrange(3, -1, -1):
                dp[j] += dp[j + 1]
        return sum(dp)
