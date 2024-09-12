class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        GATE = 0
        WALL = -1
        n = len(rooms)
        m = len(rooms[0])

        q = []

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == GATE:
                    q.append([i, j])

        while q:
            i, j = q.pop(0)
            for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                i_ = i + y
                j_ = j + x
                if not (0 <= i_ < n and 0 <= j_ < m) or not rooms[i_][j_] == INF:
                    continue
                
                rooms[i_][j_] = rooms[i][j] + 1
                q.append([ i_, j_ ])
        
