class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        n = len(nums)

        stack = []

        # next smaller element for index i
        next_stack = [-1] * n

        # prev smaller element for index i
        prev_stack = [-1] * n

        # treat i as the minimum value in the subarray and
        # find the subarray such that every element is >= nums[i]
        # use a stack to record unprocessed values

        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                next_stack[stack[-1]] = i
                stack.pop()
            
            stack.append(i)
        
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[i] < nums[stack[-1]]:
                prev_stack[stack[-1]] = i
                stack.pop()
            
            stack.append(i)
        
        for i in range(n):
            left = prev_stack[i]
            right = n if next_stack[i] == -1 else next_stack[i]

            length = right - left - 1

            if nums[i] > float(threshold / length):
                return length
            
        return -1
