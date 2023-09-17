class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: 
            return True 
        
        stack = [] 
        for c in s: 
            if c == ')' and stack and stack[-1] == '(':
                stack.pop()
            else: 
                stack.append(c) 
        return len(stack)