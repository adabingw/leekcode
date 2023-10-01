class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x 
        start = 0 

        curr_sum = 0 
        max_len = 0 

        found = False 

        for end in range(len(nums)): 
            curr_sum += nums[end] 

            while start <= end and curr_sum > target: 
                curr_sum -= nums[start] 
                start += 1 

            if curr_sum == target: 
                found = True
                max_len = max(max_len, end - start + 1)

        return len(nums) - max_len if found else -1 