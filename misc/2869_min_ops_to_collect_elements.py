class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = [i + 1 for i in range(k)]
        result = 0
        while arr:
            num = nums.pop()
            if num in arr:
                arr.pop(arr.index(num))
            result += 1
        return result
