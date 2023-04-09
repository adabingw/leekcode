class Solution(object):
    def closedIsland(self, grid):
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
            is_closed = True 
            while q: 
                i, j = q.pop(0) 
                for direction in directions: 
                    new_i = i + direction[0] 
                    new_j = j + direction[1] 
                    if not (0 <= new_i < n) or not(0 <= new_j < m): 
                        is_closed = False 
                    elif not visited[new_i][new_j] and grid[new_i][new_j] == 0:
                        q.append((new_i, new_j))
                        visited[new_i][new_j] = True 

            return is_closed

        ans = 0
        for i in range(n): 
            for j in range(m): 
                if grid[i][j] == 0 and not visited[i][j] and bfs(i, j): 
                    ans += 1 
        return ans 