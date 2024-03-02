class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        result = 0
        while target != 1:
            if maxDoubles == 0:
                result += (target - 1)
                break
            if target % 2 == 0 and maxDoubles > 0:
                result += 1
                target /= 2
                maxDoubles -= 1
            else: 
                result += 1
                target -= 1
        return result