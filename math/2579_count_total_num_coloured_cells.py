class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n * (n - 1) * 2 + 1