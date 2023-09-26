class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        curr = 0
        stack = list(t)
        while stack:
            if curr == len(s):
                return True
            if s[curr] == stack[0]:
                curr += 1
            stack.pop(0)
        return curr == len(s)
