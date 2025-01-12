class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_ = []
        t_ = []

        for i in range(len(s)):
            if s[i] == '#' and s_:
                s_.pop()
            elif s[i] != '#':
                s_.append(s[i])
        
        for i in range(len(t)):
            if t[i] == '#' and t_:
                t_.pop()
            elif t[i] != '#':
                t_.append(t[i])
        
        return s_ == t_