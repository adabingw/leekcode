class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour_ = 30 * hour + 0.5 * minutes
        minute_ = 6 * minutes

        angle = abs(hour_ - minute_)
        if angle > 180:
            angle = 360 - angle
        
        return angle
