class Solution(object):
    def maxScore(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        
        dp = [nums[0] - x, nums[0] - x] # even, odd
        if nums[0] % 2 == 0:
            dp[0] = nums[0]
        else:
            dp[1] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                dp[0] = max(dp[0], dp[1] - x) + nums[i]
            else:
                dp[1] = max(dp[1], dp[0] - x) + nums[i]
        
        return max(dp)