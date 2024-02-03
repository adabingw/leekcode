class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        max_left = max(left or [0])
        max_right = n - min(right or [n])
        return max(max_left, max_right)
