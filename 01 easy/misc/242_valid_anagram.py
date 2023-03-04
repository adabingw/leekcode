class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_sort = ''.join(sorted(str(s))) 
        t_sort = ''.join(sorted(str(t)))
        if s_sort == t_sort: 
            return True 
        else: 
            return False 