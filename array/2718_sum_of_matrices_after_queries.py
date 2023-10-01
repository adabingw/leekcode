class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """

        # previous values can be completely wiped by future values
        # iterate queries reversely
        # once value is filled, cannot be changed anymore

        # col[i] == values in row with index i
        # row[i] == values in col with index i

        col = {}
        row = {}
        result = 0
        for t, i, v in queries[::-1]:

            # there is len(col) number of columns already taken,
            # we only fill n - len(col) cells in the row
            if t == 0 and i not in row:
                row[i] = v
                result += v * (n - len(col))
            
            if t == 1 and i not in col:
                col[i] = v
                result += v * (n - len(row))
        
        return result
