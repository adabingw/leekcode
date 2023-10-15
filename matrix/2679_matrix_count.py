class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            nums[i].sort()
        
        scores = []
        for cols in range(len(nums[0])):
            for i in range(len(nums)):
                scores.append(nums[i].pop())
            result += max(scores)
            scores = []

        return result
