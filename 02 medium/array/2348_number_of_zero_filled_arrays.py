class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0 
        subarray = 0 
        for num in nums: 
            if num == 0: 
                subarray += 1 
            else: 
                subarray = 0 
            ans += subarray 
        return ans 