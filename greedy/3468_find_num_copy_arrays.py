class Solution(object):
    def countArrays(self, original, bounds):
        """
        :type original: List[int]
        :type bounds: List[List[int]]
        :rtype: int
        """
        n = len(original)
    
        # dp[i] = # valid ranges for element at i
        dp = [0] * n
        
        dp[0] = (bounds[0][0], bounds[0][1])
    
        for i in range(1, n):
            diff = original[i] - original[i-1]
            new_dp = []

            (l, r) = dp[i - 1]
            
            left = l + diff
            right = r + diff
                
            if left <= bounds[i][1] and right >= bounds[i][0]:
                left = max(left, bounds[i][0])
                right = min(right, bounds[i][1])
                
                new_dp = [(left, right)]

            if len(new_dp) == 0:
                return 0
            dp[i] = new_dp[0]

        i, j = dp[-1]
        
        return j - i + 1