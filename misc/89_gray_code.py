class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [] 
        result.append(0)

        if n == 0: 
            return result

        result.append(1) 

        mask = 1
        for i in range(2, n + 1): 
            prev = len(result)
            mask *= 2 

            for j in range(prev, 0, -1): 
                result.append(mask + result[j - 1])

        return result