class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        if k == 0:
            return nums

        res = [-1] * len(nums)

        prefix = [0] * (len(nums) + 1)
        prefix[1] = nums[0]
        for i in range(1, len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(1, len(nums) + 1):
            if k <= i - 1 < len(nums) - k:
                res[i - 1] = (prefix[i + k] - prefix[i - k - 1]) // (k * 2 + 1)
        
        return res