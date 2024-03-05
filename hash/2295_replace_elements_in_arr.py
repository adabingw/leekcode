class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        
        indices = {}
        for i, n in enumerate(nums):
            indices[n] = i
        
        for i, v in operations: 
            nums[indices[i]] = v
            indices[v] = indices[i]
        
        return nums