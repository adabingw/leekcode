class Solution(object):
    def maximumOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # double the same number k times
        # shift the leftmost bit to the left k bits
        # use suffix "sum" to calculate the xor of nums[i + 1:]
        # left calculates the xor of nums[0:i]
        # our result would be the max of result and left | nums[i] << k | right[i]

        result = 0
        left = 0
        n = len(nums)
        right = [0] * n

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] | nums[i + 1]

        for i in range(n):
            result = max(result, left | nums[i] << k | right[i])
            left = left | nums[i]
        
        return result
