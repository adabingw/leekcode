class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        s = list(s)
        i = 0
        while i < len(s):
            if s[i] == '(': 
                stack.append(i) 
            elif s[i] == ')': 
                if len(stack) == 1: 
                    s.pop(i)
                    s.pop(stack[0])
                    i -= 2
                    stack.pop() 
                elif len(stack) > 1: 
                    stack.pop()
            i += 1
        return ''.join(s)