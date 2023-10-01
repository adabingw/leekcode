class Solution(object):
    def countPairs(self, coordinates, k):
        """
        :type coordinates: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(coordinates) < 2:
            return 0
        
        result = 0
        count = Counter()

        # one pass input array
        # count frequency of array[i]
        # for each array[i], find pair that corresponds 
        # to A[i][0] ^ var + A[i][1] ^ (k - var) = k
        # update res += count[A[i][0] ^ var, A[i][1] ^ (k - var)]

        for coordinate in coordinates:
            for x in range(k + 1):
                result += count[coordinate[0] ^ x, coordinate[1] ^ (k - x)]
            count[coordinate[0], coordinate[1]] += 1        
        return result
