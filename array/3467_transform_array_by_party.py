class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zeroes = []
        ones = []

        for num in nums:
            if num % 2 != 0:
                ones.append(1)
            else:
                zeroes.append(0)

        return zeroes + ones