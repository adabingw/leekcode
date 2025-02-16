class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for i, n in enumerate(nums):
            c = 0
            if i - k >= 0:
                c = 1 if nums[i - k] < nums[i] else 0
            else:
                c += 1

            if i + k < len(nums):
                c = c + 1 if nums[i + k] < nums[i] else c
            else:
                c += 1
            if c == 2:
                res += n
        return res