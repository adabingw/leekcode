class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        subarrays = []

        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                subarrays.append(s)
        
        subarrays.sort()

        res = 0
        MOD = 10 ** 9 + 7

        for i in range(left - 1, right):
            res = (res + subarrays[i]) % MOD
        
        return res