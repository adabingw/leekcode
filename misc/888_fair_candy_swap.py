class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        aliceSizes = set(aliceSizes)
        for a in aliceSizes:
            b = a + (sum_bob - sum_alice) / 2
            if b in bobSizes:
                return [a, b]
