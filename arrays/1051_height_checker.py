class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != h[i]:
                res += 1
        return res