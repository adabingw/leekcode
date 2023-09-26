class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        result = [i for i in range(len(grid[0]))]
        for row in grid: 
            for i in range(len(result)): 
                if result[i] == -1 or result[i] < 0 or result[i] >= len(result):
                    result[i] = -1
                elif result[i] == 0 and row[result[i]] == -1:
                    result[i] = -1
                elif result[i] == len(result) - 1 and row[result[i]] == 1:
                    result[i] = -1
                elif row[result[i]] == -1 and row[result[i] - 1] == -1:
                    result[i] -= 1
                elif row[result[i]] == 1 and row[result[i] + 1] == 1:
                    result[i] += 1
                else: 
                    result[i] = -1
        return result
