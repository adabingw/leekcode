from collections import deque 

class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums) 

        # dq[0] always has the max
        dq = deque([0]) 
        for i in range(1, n): 

            # add max with current 
            nums[i] = nums[dq[0]] + nums[i]
            
            # while max <= current
            while dq and nums[dq[-1]] <= nums[i]: 
                dq.pop()

            # add current to end of dq
            dq.append(i)

            # maintain sliding window
            if i - dq[0] >= k: 
                dq.popleft() 
            
        return nums[-1]