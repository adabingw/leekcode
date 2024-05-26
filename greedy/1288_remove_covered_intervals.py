class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x: (x[0], -x[1]))
        for index, [start, end] in enumerate(intervals):
            i = index + 1
            while i < len(intervals):
                start1 = intervals[i][0]
                end1 = intervals[i][1]               
                if start <= start1 and end1 <= end:
                    del intervals[i]
                else:
                    i += 1
        return len(intervals)