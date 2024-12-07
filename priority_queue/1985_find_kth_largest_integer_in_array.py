class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        h = []
        for num in nums:
            heapq.heappush(h, int(num))
        
            if len(h) > k:
                heapq.heappop(h)

        # Return the Kth smallest element (top of the max heap, negated)
        return str(h[0])