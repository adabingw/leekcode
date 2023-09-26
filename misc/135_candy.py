class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        result = [1] * n 

        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                result[i + 1] = 1 + result[i]
        
        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                result[i] = max(1 + result[i + 1], result[i])
        
        print(result)
        return sum(result)
