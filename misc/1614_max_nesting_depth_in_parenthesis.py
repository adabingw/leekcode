class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxdepth = 0 
        depth = 0 
        for c in s: 
            if c == '(': 
                depth += 1 
                maxdepth = max(maxdepth, depth)
            if c == ')': 
                depth -= 1
        return maxdepth