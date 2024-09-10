class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """

        m = max(1, maxSum // n - (n * n))

        s = m * n

        left = index
        right = index

        res = m
        
        if n == maxSum:
            return res
        
        while s < maxSum:
            res += 1

            s += (right - left + 1)

            if s > maxSum:
                return res - 1
            
            left = left - 1 if left > 0 else 0
            right = right + 1 if right < n - 1 else n - 1
        
        return res
