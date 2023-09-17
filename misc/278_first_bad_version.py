# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: 
            return 1
        start = 0
        end = n 
        while end - start > 1: 
            mid = start + (end - start) / 2 
            if (isBadVersion(mid)):
                end = mid 
            else: 
                start = mid 
        return end 