class Solution(object):
    def maxSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        score = nums[0]
        for i in range(1, n):
            score = score & nums[i]
        
        if score != 0:
            return 1
        
        score = nums[0]
        result = 0
        for i in range(1, n):
            if score == 0:
                print(i)
                result += 1
                score = nums[i]
            else:
                score = score & nums[i]
        
        if score == 0:
            result += 1
        
        return result
