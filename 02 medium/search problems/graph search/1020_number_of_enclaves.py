class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid) 
        m = len(grid[0])

        visited = [[False] * m for i in range(n)] 
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(i, j):
            visited[i][j] = True 
            q = [(i, j)]
            area = 1
            while q: 
                i, j = q.pop(0) 
                for direction in directions: 
                    new_i = i + direction[0] 
                    new_j = j + direction[1] 
                    if not (0 <= new_i < n) or not(0 <= new_j < m): 
                        continue
                    elif not visited[new_i][new_j] and grid[new_i][new_j] == 1:
                        q.append((new_i, new_j))
                        visited[new_i][new_j] = True 

            return

        for i in range(n): 
            if grid[i][0] == 1 and not visited[i][0]: 
                bfs(i, 0) 
            if grid[i][m - 1] == 1 and not visited[i][m - 1]: 
                bfs(i, m - 1)
        
        for i in range(m): 
            if grid[0][i] == 1 and not visited[0][i]: 
                bfs(0, i) 
            if grid[n - 1][i] == 1 and not visited[n - 1][i]: 
                bfs(n - 1, i)

        ans = 0
        for i in range(n): 
            for j in range(m): 
                if grid[i][j] == 1 and not visited[i][j]: 
                    ans += 1
        return ans