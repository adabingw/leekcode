class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # unserious answer 1
        # s.reverse()

        # unserious answer 2
        # s[:] = [::-1]

        n = len(s)

        def reverse(i):
            if i == n:
                while len(s) != n:
                    s.pop()
                return s
            
            s.insert(i, s[-1 * (i + 1)])
            reverse(i + 1)
        
        reverse(0)