class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        bfs = []
        n = len(grid)
        m = len(grid[0])
        cost = 0
        dp = [[float('inf')] * m for _ in range(n)]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < m and dp[i][j] == float('inf')):
                return
            dp[i][j] = cost
            bfs.append([i, j])
            dfs(i + directions[grid[i][j] - 1][0], j + directions[grid[i][j] - 1][1])
        
        dfs(0, 0)
        while bfs:
            cost += 1
            bfs2 = bfs
            bfs = []

            for i, j in directions:
                for x, y in bfs2:
                    dfs(x + i, y + j)

        return dp[-1][-1]
