class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(len(nums) - 1):
            prefix[i + 1] = prefix[i] * nums[i + 1]
            suffix[-1 - 1 - i] = suffix[-1 - i] * nums[-1 - 1 - i]
        for i, n in enumerate(nums): 
            result[i] = (prefix[i - 1] if i > 0 else 1) * (suffix[i + 1] if i < len(nums) - 1 else 1)
        return result
