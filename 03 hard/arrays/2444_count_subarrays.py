class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        number = 0 
        min_index = -1 
        max_index = -1
        start = 0
        for i in range(len(nums)): 
            if not minK <= nums[i] <= maxK: 
                start = i + 1 
                min_index = -1 
                max_index = -1
            if nums[i] == minK: 
                min_index = i 
            if nums[i] == maxK: 
                max_index = i 
            if min_index != -1 and max_index != -1: 
                number += min(min_index, max_index) - start + 1 
        return number