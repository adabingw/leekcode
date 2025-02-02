class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        found_start = False
        n = len(nums)

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                if found_start:
                    return False
                found_start = True
        
        return not found_start or nums[0] >= nums[n - 1]