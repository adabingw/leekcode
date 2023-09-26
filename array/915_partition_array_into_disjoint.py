class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        min_num = [float('inf')] * n
        min_num[-1] = nums[-1]

        max_num = [0] * n
        max_num[0] = nums[0]

        for i in range(n - 2, -1, -1):
            min_num[i] = min(min_num[i + 1], nums[i])
        
        for i in range(1, n):
            max_num[i] = max(max_num[i - 1], nums[i])

        for i in range(0, n - 1):
            if max_num[i] <= min_num[i + 1]:
                return i + 1
