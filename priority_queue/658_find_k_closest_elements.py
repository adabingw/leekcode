class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        h = []

        for a in arr:
            heappush(h, (abs(a - x), a))
        
        r = []

        for i in range(k):
            r.append(heappop(h)[1])
        
        r.sort()
        return r