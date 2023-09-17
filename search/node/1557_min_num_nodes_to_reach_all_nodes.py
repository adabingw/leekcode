class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        edge_exists = [False] * n

        for edge in edges: 
            edge_exists[edge[1]] = True 
        
        result = []

        for index, existing in enumerate(edge_exists): 
            if existing is False: 
                result.append(index)

        return result