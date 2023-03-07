class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        def validateTime(givenTime): 
            trips = 0 
            for t in time: 
                trips += givenTime // t 
            return trips >= totalTrips 

        left = 1 
        right = max(time) * totalTrips 

        while left < right: 
            mid = (left + right) // 2 
            if validateTime(mid): 
                right = mid
            else: 
                left = mid + 1 
        return left 