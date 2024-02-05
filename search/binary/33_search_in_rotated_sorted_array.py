class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1 and nums[0] == target:
            return 0
        elif len(nums) == 1 and nums[0] != target:
            return -1

        l = 0
        r = len(nums)

        while l < r:
            m = (r + l) // 2

            if nums[m] == target:
                return m

            # target rotated to the right
            if target < nums[0] < nums[m]: # -inf
                l = m + 1

            # target rotated to the left
            elif target >= nums[0] > nums[m]: # +inf
                r = m

            # target is larger than m and to the right of it
            elif nums[m] < target:
                l = m + 1

            # target is less than m and to the left of it
            elif nums[m] > target:
                r = m

        return -1
