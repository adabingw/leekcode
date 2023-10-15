class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix) 
        n = len(matrix[0])

        y = set()
        x = set()

        for i, row in enumerate(matrix): 
            for j, element in enumerate(row): 
                if element == 0: 
                    y.add(i) 
                    x.add(j)

        for row in y: 
            matrix[row] = [0] * n 
        
        for i, row in enumerate(matrix): 
            for col in x: 
                matrix[i][col] = 0


        print(matrix)