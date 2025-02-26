class Solution:
    def maxAbsoluteSum(self, nums):
        min_prefix_sum = float("inf")
        max_prefix_sum = float("-inf")
        prefix_sum = 0
        res = 0

        for num in nums:
            prefix_sum += num

            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)

            if prefix_sum >= 0:
                res = max(res, max(prefix_sum, prefix_sum - min_prefix_sum))
            elif prefix_sum <= 0:
                res = max(res, max(abs(prefix_sum), abs(prefix_sum - max_prefix_sum)),)

        return res