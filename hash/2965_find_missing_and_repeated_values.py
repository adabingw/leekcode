class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        freq = defaultdict(int)

        for row in grid:
            for num in row:
                freq[num] += 1
        
        for i in range(1, n * n + 1):
            if not freq[i]:
                missing = i
            elif freq[i] == 2:
                repeat = i
        
        return [repeat, missing]