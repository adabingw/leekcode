class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """

        c = collections.Counter(changed)
    
        if c[0] % 2:
            return []

        for i in sorted(c):
            if c[i] > c[2 * i]:
                return []
            
            # if i == 0, then we want to keep half of the elements
            c[2 * i] -= c[i] if i else c[i] / 2

        return list(c.elements())