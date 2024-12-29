class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        n = (len(b) - 1) // (len(a)) + 1
        for i in range(2):
            if b in a * (n + i):
                return n + i
        
        return -1