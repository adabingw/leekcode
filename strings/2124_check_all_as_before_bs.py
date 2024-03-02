class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = False
        for s1 in s:
            if s1 == 'b':
                b = True
            
            if s1 == 'a' and b:
                return False
        
        return True