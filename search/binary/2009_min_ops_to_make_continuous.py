class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        result = n
        new_nums = sorted(set(nums))
        
        for i in range(len(new_nums)):
            left = new_nums[i]
            right = left + n - 1

            # use binary search to find how many elements
            # less than or equal to right
            j = bisect_right(new_nums, right)
            count = j - i
            
            result = min(result, n - count)

        return result
