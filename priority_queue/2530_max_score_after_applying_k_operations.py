class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [ -n for n in nums ]
        heapify(nums)
        res = 0
        for i in range(k):
            n = -heappop(nums)
            res += n
            heappush(nums, (n // -3))
        return res