class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        h = [] # (value, list index, element index)
        n = len(nums)
        max_val = float('-inf')
        range_start = 0
        range_end = float('inf')

        # insert first elem from each list into heap
        for i in range(n):
            heapq.heappush(h, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])

        while len(h) == n:
            min_val, row, col = heapq.heappop(h)

            # update smallest range
            if max_val - min_val < range_end - range_start:
                range_start = min_val
                range_end = max_val
            
            # add next element from same row into heap
            if col + 1 < len(nums[row]):
                next_val = nums[row][col + 1]
                heapq.heappush(h, (next_val, row, col + 1))
                max_val = max(max_val, next_val)
        
        return [range_start, range_end]