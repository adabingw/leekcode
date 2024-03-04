class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()

        result = 0

        child = 0
        cookie = 0
        
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                result += 1
                child += 1
                cookie += 1
            else:
                cookie += 1
        
        return result
            
