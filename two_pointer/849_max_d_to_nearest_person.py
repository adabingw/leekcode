class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        left = -1
        result = 0
        leftfound = False
        for i, seat in enumerate(seats):
            if i == len(seats) - 1 and seat == 0:
                result = max(result, i - left)
            elif seat == 1 and not leftfound:
                if left == -1:
                    result = max(result, i)
                left = i
            elif seat == 1 and leftfound:
                result = max(result, (i - left) / 2)
                leftfound = False
                left = i
            elif seat == 0 and left != -1: 
                leftfound = True

        return result
