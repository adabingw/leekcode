class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], K: int) -> int:
        n = len(piles)

        @lru_cache(None)
        def dp(i, k):
            if k == 0 or i == n: 
                return 0

            res, cur = dp(i + 1, k), 0

            for j in range(min(len(piles[i]), k)):
                cur += piles[i][j]
                res = max(res, cur + dp(i + 1, k - j - 1))
            return res
        
        return dp(0, K)