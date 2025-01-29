class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(isWater)
        m = len(isWater[0])

        q = deque()

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                new_i = i + x
                new_j = j + y

                if 0 <= new_i < n and 0 <= new_j < m and isWater[new_i][new_j] == 0:
                    isWater[new_i][new_j] = isWater[i][j] + 1
                    q.append((new_i, new_j))
        
        for i in range(n):
            for j in range(m):
                isWater[i][j] -= 1
        
        return isWater