class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        count = defaultdict(int)
        for a in arr:
            count[a] += 1
        
        heap = []
        for c in count:
            heappush(heap, (count[c], c))
                
        while k > 0:
            if not heap:
                return 0

            c, num = heappop(heap)
            if c > k:
                heappush(heap, (c - k, num))
                k = 0
            else: 
                k = k - c
        
        return len(heap)