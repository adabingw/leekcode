class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """

        heap = []
        
        for i in range(len(heights) - 1):
            # gap between next building and current building
            h = heights[i + 1] - heights[i]

            # if gap is positive (next building taller)
            if h > 0:

                # add gap to heap
                heapq.heappush(heap, h)

            # used up all the ladders, need to allocate bricks
            if len(heap) > ladders:

                # choose the building with the least amount of bricks needed
                bricks -= heapq.heappop(heap)
            
            # used too much bricks
            if bricks < 0:
                return i
        
        return len(heights) - 1