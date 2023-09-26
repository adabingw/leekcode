class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_bracket = 0
        for s1 in s:
            if s1 == ']' and open_bracket > 0:
                open_bracket -= 1
            elif s1 == '[':
                open_bracket += 1
        
        return (open_bracket + 1) // 2
