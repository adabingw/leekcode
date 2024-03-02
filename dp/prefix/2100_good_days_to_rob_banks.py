class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """
        if time >= len(security):
            return []
        
        n = len(security)
        result = []
        
        before = [0] * n
        after = [0] * n

        for i in range(1, n):
            before[i] = before[i - 1] + 1 if security[i] <= security[i - 1] else before[i]
        
        for i in range(n - 2, -1, -1):
            after[i] = after[i + 1] + 1 if security[i] <= security[i + 1] else after[i]
        
        for i in range(time, n - time):
            if before[i] >= time and after[i] >= time:
                result.append(i)

        return result