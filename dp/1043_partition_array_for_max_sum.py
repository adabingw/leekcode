class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        n = len(arr)
        dp = [0] * (n + 1)
        for i in xrange(1, n + 1):
            curr_max = 0
            for j in xrange(1, min(k, i) + 1):
                curr_max = max(curr_max, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + curr_max * j)
        return dp[n]
        