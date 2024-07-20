class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()

        # calculate num balls placed in baskets
        # where minimum distance between any 2 balls is d
        # aim for result == m
        def minDist(d):
            res = 1
            curr = position[0]
            for i in range(1, len(position)):
                if position[i] - curr >= d:
                    res += 1
                    curr = position[i]
            return res

        l = 0
        r = position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if minDist(mid) >= m:
                l = mid
            else:
                r = mid - 1
        
        return l