class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        piles = [pile * -1 for pile in piles]
        heapq.heapify(piles)

        while k:
            pile = heapq.heappop(piles)
            new_pile =  -((pile * -1) // -2)
            heapq.heappush(piles, new_pile * -1)
            k -= 1

        result = int(abs(sum(list(piles))))
        return result