class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def validateK(k): 
            hours = 0 
            for pile in piles: 
                hours += (pile + k - 1) / mid
            return hours > h

        left = 1
        right = max(piles) 

        while left < right:
            mid = (left + right) / 2
            if validateK(mid): 
                left = mid + 1
            else: 
                right = mid
        
        return left