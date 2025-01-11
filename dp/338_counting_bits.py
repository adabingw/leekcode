class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0] * (n + 1)
        i = 2
        j = 0

        for k in range(1, n + 1):
            if k == i:
                i *= 2
                j = 0

            dp[k] = dp[j] + 1
            j += 1
        return dp