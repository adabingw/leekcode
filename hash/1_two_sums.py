class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num = {}
        for i in range(len(nums)): 
            if target - nums[i] in num:
                return [i, num[target - nums[i]]]
            num[nums[i]] = i
