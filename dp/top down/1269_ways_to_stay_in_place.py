class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(curr, remain):
            if remain == 0:
                return curr == 0
            
            # stay
            result = dp(curr, remain - 1)

            # go left
            if curr > 0:
                result = (result + dp(curr - 1, remain - 1)) % MOD
            
            # go right
            if curr < arrLen - 1:
                result = (result + dp(curr + 1, remain - 1)) % MOD

            return result
        
        return dp(0, steps) % MOD
