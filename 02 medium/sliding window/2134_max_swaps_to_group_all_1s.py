class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        window = sum(num == 1 for num in nums)
        nums += nums 
        result = window 
        zeroes = sum(num == 0 for num in nums[:window])

        for i in range(window, len(nums)): 
            zeroes -= (nums[i - window] == 0) 
            zeroes += (nums[i] == 0)
            result = min(result, zeroes)

        return result