class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        result = [0] * (n + 1)
        result[1] = 1
        for i in range(1, n / 2 + 1):
            result[2 * i] = result[i]
            if not 2 * i + 1 > n:
                result[2 * i + 1] = result[i] + result[i + 1]
        return max(result)
