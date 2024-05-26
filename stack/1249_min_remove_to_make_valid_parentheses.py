class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        result = 0
        i = 0
        s = list(s)
        while i < len(s):
            if s[i] == '(':
                stack.append(i)
                i += 1
            elif s[i] == ')':
                if stack:
                    stack.pop()
                    i += 1
                else: 
                    s.pop(i)
            else:
                i += 1
        while stack:
            s.pop(stack.pop())
        return ''.join(s)