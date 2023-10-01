class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        result = 0
        last_0 = -1
        for right in range(len(nums)):
            if nums[right] == 0:
                left = last_0 + 1
                last_0 = right
            result = max(result, right - left)
        return result 
