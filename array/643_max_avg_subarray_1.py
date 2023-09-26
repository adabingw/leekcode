class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        result = sum(nums[0:k])
        curr = result
        for i in range(len(nums) - k):
            curr += + nums[i + k] - nums[i]
            result = max(curr, result)
        return float(result) / k
