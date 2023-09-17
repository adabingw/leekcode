class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [] 
        for c in s: 
            if c.isupper() and stack and stack[-1] == c.lower(): 
                stack.pop() 
            elif c.islower() and stack and stack[-1] == c.upper(): 
                stack.pop()
            else: 
                stack.append(c)
        return ''.join(stack)