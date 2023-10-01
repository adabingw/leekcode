class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        def rob1(arr):
            n = len(arr)
            if n == 1:
                return arr[0]

            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])
            return dp[n - 1]

        return max(rob1(nums[1:]), rob1(nums[:-1]))
