class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        drops = 1
        while result < n:
            result += drops
            drops += 1
        return drops - 1
