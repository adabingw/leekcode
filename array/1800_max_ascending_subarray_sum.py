class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        inc = nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                inc += nums[i + 1]
            else:
                res = max(res, inc)
                inc = nums[i + 1]
        
        return max(res, inc)