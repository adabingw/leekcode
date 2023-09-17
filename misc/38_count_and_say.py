class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1: 
            return '1'

        s = ['1']

        for i in range(1, n):
            j = 0
            while j < len(s):
                letter = s[j] 
                k = j + 1
                count = 1
                while k < len(s) and s[k] == letter: 
                    count += 1
                    del s[k]

                s.insert(j, str(count))
                j += 2
                    
        return ''.join(s)
    