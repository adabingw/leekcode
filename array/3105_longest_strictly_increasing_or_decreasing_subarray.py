class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inc = 1
        dec = 1
        max_len = 1

        for pos in range(len(nums) - 1):
            if nums[pos + 1] > nums[pos]:
                inc += 1
                dec = 1
            elif nums[pos + 1] < nums[pos]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1

            max_len = max(max_len, inc, dec)
        
        return max_len