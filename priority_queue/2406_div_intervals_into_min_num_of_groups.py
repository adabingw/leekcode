class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        groups = []

        for i, j in intervals:
            # if our current start is greater than the smallest value
            # in the heap, then we add this to the same group
            if groups and i > groups[0]:
                heapq.heappop(groups)
            
            heapq.heappush(groups, j)
        
        return len(groups)