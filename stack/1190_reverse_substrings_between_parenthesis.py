class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = ['']
        for i, s1 in enumerate(s):
            if s1 == '(':
                stack.append('')
            elif s1 == ')':
                stack[len(stack) - 2] += stack.pop()[::-1]
            else:
                stack[-1] += str(s1)
        return "".join(stack)