class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for s1 in s:
            if s1.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(s1)
        
        return ''.join(stack)