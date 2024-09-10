class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        t = 0
        n = len(grid)
        m = len(grid[0])
        q = []
        visited = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    visited[i][j] = True
                    q.append((i, j))
        
        while q:
            new_q = []
            t += 1
            for i, j in q:
                grid[i][j] = 2
                for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    new_i, new_j = i + x, j + y
                    if new_i >= 0 and new_i < n and new_j >= 0 and new_j < m:
                        if grid[new_i][new_j] == 1:
                            grid[new_i][new_j] = 2
                            new_q.append((new_i, new_j))
            q = new_q

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return t - 1 if t > 0 else 0
