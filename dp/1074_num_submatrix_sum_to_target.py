class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        
        # for each row, calculate the prefix sum
        # for each col, calculate the accumulated sum of rows
        # now it's basically "find subarray with target sum"

        n = len(matrix)
        m = len(matrix[0])

        for row in matrix:
            for i in xrange(m - 1):
                row[i + 1] += row[i]
        
        print(matrix)

        result = 0
        for i in range(m):
            for j in range(i, m):
                c = defaultdict(int)
                curr = 0
                c[0] = 1
                for k in range(n):
                    curr += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    result += c[curr - target]
                    c[curr] += 1
        return result
