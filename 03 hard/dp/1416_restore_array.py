class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        m = len(s)
        dp = [0] * (m + 1)
        mod = 10 ** 9 + 7

        def dfs(start): 
            if dp[start]: 
                return dp[start] 
            if start == m: 
                return 1 
            if s[start] == '0': 
                return 0 
            
            count = 0 
            for end in range(start, m): 
                if int(s[start : end + 1]) > k: 
                    break
                count += dfs(end + 1)
            
            dp[start] = count % mod
            return count
        
        return dfs(0) % mod