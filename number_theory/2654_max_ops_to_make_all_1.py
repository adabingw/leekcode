class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = nums.count(1)
        if ones > 0: 
            return len(nums) - ones
        
        # len of smallest subarray of gcd 1
        subarray = float('inf')

        def gcd(x, y):
            while y != 0:
                (x, y) = (y, x % y)
            return x

        for i in range(len(nums)):
            divisor = nums[i]
            for j in range(i + 1, len(nums)):
                divisor = gcd(divisor, nums[j])
                if divisor == 1:
                    subarray = min(subarray, j - i)
        
        return -1 if subarray == float('inf') else subarray + len(nums) - 1
