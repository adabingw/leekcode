class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = copy.deepcopy(nums)
        for i in range(1, len(nums)): 
            dp[i] = max(nums[i], nums[i] + dp[i - 1]) 
        return max(dp)