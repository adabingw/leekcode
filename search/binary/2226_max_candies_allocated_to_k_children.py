class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        candies.sort()

        if sum(candies) < k:
            return 0
        
        left = 0
        right = max(candies)

        def can_allocate(m):
            res = 0

            for candy in candies:
                res += candy // m
            
            return res >= k

        while left < right:
            middle = (left + right + 1) // 2

            if can_allocate(middle):
                left = middle
            else:
                right = middle - 1
        
        return left