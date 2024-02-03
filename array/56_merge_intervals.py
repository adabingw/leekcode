class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals = sorted(intervals)
        result = []

        curr_max = intervals[0][1]
        curr_min = intervals[0][0]
        
        for interval in intervals:
            if interval[0] <= curr_max:
                curr_max = max(curr_max, interval[1])
            else:
                result.append([curr_min, curr_max])
                curr_min = interval[0]
                curr_max = interval[1]

        result.append([curr_min, curr_max])

        print(result)
        return result
