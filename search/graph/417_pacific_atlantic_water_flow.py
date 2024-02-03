class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(heights)
        m = len(heights[0])
        result = []
        self.pacific = False
        self.atlantic = False
        self.visited = [[False] * m for i in range(n)]

        def dfs(i, j):
            self.visited[i][j] = True
            for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                new_i, new_j = i + x, j + y
                if new_i < 0 or new_j < 0:
                    self.pacific = True
                    continue
                if new_i >= n or new_j >= m:
                    self.atlantic = True
                    continue
                if self.pacific and self.atlantic:
                    self.visited[i][j] = False
                    return
                if heights[i][j] >= heights[new_i][new_j] and not self.visited[new_i][new_j]:
                    dfs(new_i, new_j)
            self.visited[i][j] = False
            return

        if n == 1 or m == 1:
            for i in range(n):
                for j in range(m):
                    result.append([i, j])
            return result
        
        for i in range(n): 
            for j in range(m): 
                dfs(i, j)
                if self.pacific and self.atlantic: 
                    result.append([i, j])
                self.pacific = False 
                self.atlantic = False
        return result
