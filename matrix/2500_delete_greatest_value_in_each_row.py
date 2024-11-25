class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        m = len(grid[0])
        n = len(grid)
        for i, r in enumerate(grid):
            heapify(grid[i])

        for i in range(m):
            item = 0
            for j in range(n):
                item = max(item, heappop(grid[j]))
            res += item
        
        return res