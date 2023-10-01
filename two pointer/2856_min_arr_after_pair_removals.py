class Solution(object):
    def minLengthAfterRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        n = len(nums)
        mid = n // 2

        right = n - 1
        left = mid - 1
        removals = 0

        while left >= 0:
            if nums[right] > nums[left]:
                removals += 2
                right -= 1
            left -= 1
        
        return n - removals
