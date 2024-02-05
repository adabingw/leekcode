class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            # m is minimum number
            if m > 0 and nums[m - 1] > nums[m]:
                return nums[m]
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return nums[m]
