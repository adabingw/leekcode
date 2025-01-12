class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for i in nums:
            i = abs(i)
            if nums[i - 1] < 0:
                res.append(i)
            nums[i - 1] *= -1
        return res