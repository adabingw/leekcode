class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # TLE Solution
        # left = 0 
        # right = k

        # result = []

        # while right < len(nums) + 1: 
        #     result.append(max(nums[left:right])) 

        #     left += 1 
        #     right += 1
        
        # return result

        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out