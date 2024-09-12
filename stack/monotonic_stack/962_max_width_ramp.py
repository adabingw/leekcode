class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = []
        res = 0

        # decreasing monotonic stack
        for i, n in enumerate(nums):
            if not stack or nums[stack[-1]] > n:
                stack.append(i)
        
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                res = max(res, j - stack.pop())

        return res