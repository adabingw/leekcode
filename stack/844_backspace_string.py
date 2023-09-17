class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s = []
        stack_t = [] 
        for c in s: 
            if c == '#' and stack_s: 
                stack_s.pop() 
            elif c.isalpha(): 
                stack_s.append(c) 
        
        for d in t: 
            if d == '#' and stack_t: 
                stack_t.pop() 
            elif d.isalpha(): 
                stack_t.append(d)

        return ''.join(stack_s) == ''.join(stack_t)