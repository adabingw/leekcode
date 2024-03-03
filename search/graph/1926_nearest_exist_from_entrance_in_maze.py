class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        n = len(maze)
        m = len(maze[0])
        
        visited = [[False for i in range(m)] for j in range(n)]
        visited[entrance[0]][entrance[1]] = True
        q = [entrance]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0

        while q:
            new_q = []
            for e in q:
                if (e[0] == 0 or e[1] == 0 or e[0] == n - 1 or e[1] == m - 1) and e != entrance:
                    return d
                for i, j in directions: 
                    new_i = e[0] + i
                    new_j = e[1] + j
                    if 0 <= new_i < n and 0 <= new_j < m and not visited[new_i][new_j] and maze[new_i][new_j] != "+":
                        new_q.append([new_i, new_j])
                        visited[new_i][new_j] = True
            q = new_q
            d += 1
        
        return -1