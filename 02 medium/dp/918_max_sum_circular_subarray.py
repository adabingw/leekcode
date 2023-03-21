import copy

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        normalmax = copy.deepcopy(nums)
        normalmin = copy.deepcopy(nums)
        total = nums[0]
        for i in range(1, len(nums)): 
            total += nums[i]
            normalmax[i] = max(nums[i], nums[i] + normalmax[i - 1]) 
            normalmin[i] = min(nums[i], nums[i] + normalmin[i - 1]) 
        maxsum = max(normalmax)
        minsum = min(normalmin)

        print(maxsum, minsum, total)

        if total == minsum: 
            return maxsum 
        else: 
            return max(maxsum, total - minsum)
        


