class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetings.sort()
        res = 0
        curr_day = 0

        for s, e in meetings:
            if s > curr_day + 1:
                res += (s - curr_day) - 1
            
            curr_day = max(curr_day, e)
        
        res += days - curr_day

        return res