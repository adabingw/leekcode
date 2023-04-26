class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        transposed = zip(*matrix) 
        print(transposed)
        for index, row in enumerate(transposed): 
            # print(index, row)
            matrix[index] = reversed(row)
            # for m in matrix[index]:
            #     print(m) 
