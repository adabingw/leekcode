class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        res = []

        while a or b:
            if len(res) >= 2 and res[-1] == res[-2]:
                writeA = res[-1] == 'b'
            else:
                writeA = a >= b
            
            if writeA:
                a -= 1
                res.append('a')
            else:
                b -= 1
                res.append('b')
        
        return ''.join(res)