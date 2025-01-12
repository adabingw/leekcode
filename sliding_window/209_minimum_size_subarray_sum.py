class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        res = float('inf')
        left = 0
        s = 0

        if sum(nums) < target:
            return 0

        for i in range(len(nums)):
            if nums[i] >= target:
                return 1
            
            s += nums[i]

            if s >= target:
                while left < len(nums) and s >= target:
                    s -= nums[left]
                    left += 1
                res = min(res, i - left + 2)

        return res