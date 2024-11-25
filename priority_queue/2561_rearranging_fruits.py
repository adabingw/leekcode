class Solution(object):
    def minCost(self, basket1, basket2):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        c1, c2 = Counter(basket1), Counter(basket2)
        m = min(min(basket1), min(basket2))
        h = []

        for i in c1.keys():
            if c1[i] > c2[i]:
                diff = c1[i] - c2[i]
                if diff % 2:
                    return -1
                for _ in range(diff // 2):
                    heappush(h, i)
        
        for i in c2.keys():
            if c2[i] > c1[i]:
                diff = c2[i] - c1[i]
                if diff % 2:
                    return -1
                for _ in range(diff // 2):
                    heappush(h, i)
        
        n, res = len(h), 0
        for _ in range(n // 2):
            res += min(2 * m, heappop(h))
        return res