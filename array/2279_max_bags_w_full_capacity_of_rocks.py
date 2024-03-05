class Solution(object):
    def maximumBags(self, capacity, rocks, a):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        n = len(rocks)
        diff = [0] * n

        for i in range(n):
            diff[i] = capacity[i] - rocks[i]
        
        diff.sort()
        result = 0

        for i in range(n):
            if diff[i] == 0:
                result += 1
            else:
                if diff[i] > a:
                    break
                a -= diff[i]
                result += 1
        
        return result