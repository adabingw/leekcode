class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0] * n for _ in range(n)]
        
        i, j, di, dj = 0, 0, 0, 1
        for k in range(1, n*n + 1):
            result[i][j] = k
            if result[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return result