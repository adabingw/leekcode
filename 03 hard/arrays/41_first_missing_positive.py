class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 

        latest = 0

        nums = set(nums) 
        nums = list(nums)
        nums.sort()
        nums = [item for item in nums if item > 0]
        
        if not nums: 
            return 1

        for num in nums: 
            if latest != num - 1: 
                return latest + 1
            latest += 1
        return list(nums)[-1] + 1