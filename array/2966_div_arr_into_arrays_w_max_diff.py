class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for m in range(0, len(nums), 3):
            i = nums[m]
            ii = nums[m + 1]
            iii = nums[m + 2]
            if iii - ii > k or iii - i > k or ii - i > k:
                return []
            else: 
                result.append([i, ii, iii])
        return result
