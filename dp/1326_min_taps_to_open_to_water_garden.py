class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        dp = [0] + [n + 2] * n
        for i, v in enumerate(ranges):
            for j in xrange(max(i - v + 1, 0), min(i + v, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - v)] + 1)
        if dp[n] < n + 2:
            return dp[n]
        return -1
