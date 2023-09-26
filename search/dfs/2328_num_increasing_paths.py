class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        # since next step must be larger, there is no chance of 
        # revisiting a cell
        
        @lru_cache(None)
        def dfs(i, j):
            res = 1
            for i2, j2 in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]) and grid[i2][j2] < grid[i][j]:
                    res += dfs(i2, j2) % MOD
            return res

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += dfs(i, j)

        return result % MOD
