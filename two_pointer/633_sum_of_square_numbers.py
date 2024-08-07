class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = math.ceil(c ** 0.5)

        while left <= right:
            s = left ** 2 + right ** 2
            if s == c:
                return True
            
            if c > s:
                left += 1
            elif c < s:
                right -= 1
        
        return False