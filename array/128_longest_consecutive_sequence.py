class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        result = 0
        nums = set(nums)

        for x in nums:
            if x - 1 not in nums:

                y = x + 1
                while y in nums:
                    y += 1
                
                result = max(result, y - x)
            
        return result
