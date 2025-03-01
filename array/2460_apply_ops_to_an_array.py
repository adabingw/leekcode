class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []

        for i in range(0, n - 1):
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0
            
        for num in nums:
            if num != 0:
                res.append(num)
        
        while len(res) < n:
            res.append(0)
        
        return res