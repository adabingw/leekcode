class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapify(nums)
        res = 0

        while nums[0] < k and len(nums) >= 2:
            i = heappop(nums)
            j = heappop(nums)

            val = min([i, j]) * 2 + max([i, j])
            heappush(nums, val)
            res += 1
        
        return res
        
