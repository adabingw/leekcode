class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(bool)
        res = -1
        for num in nums:
            if d[num * -1]:
                res = max(res, abs(num))
            
            d[num] = True
        return res