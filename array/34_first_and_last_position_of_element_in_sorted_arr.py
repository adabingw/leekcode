class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pair = [] 
        for index, num in enumerate(nums): 
            if num == target: 
                pair.append(index) 
                break
        
        for i in range(len(nums) - 1, -1, -1): 
            if nums[i] == target: 
                pair.append(i) 
                break
        
        return pair if len(pair) == 2 else [-1, -1]
