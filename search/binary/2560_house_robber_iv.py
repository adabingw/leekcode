class Solution:
    def minCapability(self, nums, k):
        # Store the maximum nums value in maxReward.
        lo, hi = 1, max(nums)
        houses = len(nums)

        # Use binary search to find the minimum reward possible.
        while lo < hi:
            m = (lo + hi) // 2
            possible_thefts = 0

            i = 0
            while i < houses:
                if nums[i] <= m:
                    possible_thefts += 1
                    i += 2  # Skip the next house to maintain the non-adjacent condition
                else:
                    i += 1

            if possible_thefts >= k:
                hi = m
            else:
                lo = m + 1

        return lo