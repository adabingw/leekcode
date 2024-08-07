class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue

                if i == 0:
                    res += 1
                    res = res if i != n - 1 and grid[i + 1][j] == 1 else res + 1
                elif i == n - 1:
                    res += 1
                    res = res if grid[i - 1][j] == 1 else res + 1
                else:
                    res = res if grid[i - 1][j] == 1 else res + 1
                    res = res if grid[i + 1][j] == 1 else res + 1

                if j == 0:
                    res += 1
                    res = res if j != m - 1 and grid[i][j + 1] == 1 else res + 1
                elif j == m - 1:
                    res += 1
                    res = res if grid[i][j - 1] == 1 else res + 1
                else:
                    res = res if grid[i][j + 1] == 1 else res + 1
                    res = res if grid[i][j - 1] == 1 else res + 1

        return res