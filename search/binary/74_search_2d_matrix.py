class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        n = len(matrix)
        m = len(matrix[0])

        l = 0
        r = m * n - 1

        # n * m matrix convert to array => matrix[x][y] => a[x * m + y]
        # arr converted to n * m => a[x] => matrix[x / m][x % m]

        while l != r:
            mid = (l + r - 1) // 2
            if matrix[mid / m][mid % m] < target:
                l = mid + 1
            else:
                r = mid
        
        return matrix[r / m][r % m] == target
