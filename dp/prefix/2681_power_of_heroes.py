class Solution(object):
    def sumOfPower(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sum of product of max^2 and min of all non empty subsequences in the array

        MOD = 10**9 + 7
        pre = 0
        result = 0
        nums.sort()

        for index, num in enumerate(nums):
            result += num ** 3
            result += (num ** 2 * pre)
            pre = (pre * 2 + num) % MOD
        
        return result % MOD
