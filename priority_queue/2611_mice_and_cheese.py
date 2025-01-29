class Solution(object):
    def miceAndCheese(self, r1, r2, k):
        """
        :type reward1: List[int]
        :type reward2: List[int]
        :type k: int
        :rtype: int
        """
        m = len(r1) - k
        res = 0
        h = [(r1[i] - r2[i], r1[i], r2[i]) for i in range(len(r1))]
        heapify(h)

        while m > 0:
            num = heappop(h)
            res += num[2]
            m -= 1
        
        while k > 0:
            res += heappop(h)[1]
            k -= 1
        
        return res