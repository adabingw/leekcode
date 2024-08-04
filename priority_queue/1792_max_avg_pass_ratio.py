class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """

        def gain(p, t):
            return ((p + 1) / (t + 1)) - (p / t)
        
        heap = []

        for p, t in classes:
            heap.append((-gain(float(p), float(t)), float(p), float(t)))
        
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            heapq.heappush(heap, (-gain(p + 1, t + 1), p + 1, t + 1))
        
        return sum((p / t) for g, p, t in heap) / len(classes)
