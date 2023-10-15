class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])
        
        rows = defaultdict(int)
        cols = defaultdict(int)
        elements = defaultdict(list)

        for i, r in enumerate(mat):
            for j, c in enumerate(r):
                elements[c] = [i, j]
            
        for i, a in enumerate(arr):
            row, col = elements[a]
            rows[row] += 1
            cols[col] += 1

            if rows[row] == n or cols[col] == m:
                return i
        
        return len(arr) - 1
