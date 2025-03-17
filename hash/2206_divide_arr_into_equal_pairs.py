class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = Counter(nums)
        for i in c:
            if c[i] % 2 != 0:
                return False
        return True