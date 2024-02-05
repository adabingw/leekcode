class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        # time needed to arrive the target
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]


        res = slowest = 0
        for t in time[::-1]:
            if t > slowest:
                # new fleet
                res += 1
                slowest = t
        return res
