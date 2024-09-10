class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])
        res = []

        for start, end in intervals:
            found = False
            for i, v in enumerate(res):
                if v[1] <= start:
                    res[i][1] = end
                    found = True
                    break
            if not found:
                res.append([start, end])
        return len(res)
