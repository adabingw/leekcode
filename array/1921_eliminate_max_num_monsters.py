class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        times = []
        for i in range(len(dist)):
            times.append(math.ceil(float(dist[i]) / float(speed[i])))
        times.sort()
        result = 0
        print(times)
        for i, t in enumerate(times):
            if t <= i:
                break 
            result += 1
        return result
