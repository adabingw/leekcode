class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_swaps = float('inf')
        total = sum(nums)
        ones = nums[0]
        end = 0

        for start in range(len(nums)):

            if start != 0: # shift window
                ones -= nums[start - 1]
            
            while end - start + 1 < total:
                end += 1
                ones += nums[end % len(nums)]
            
            min_swaps = min(min_swaps, total - ones)
        
        return min_swaps