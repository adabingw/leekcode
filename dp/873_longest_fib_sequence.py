class Solution:
    def lenLongestFibSubseq(self, arr):
        n = len(arr)
        res = 0

        # dp[i][j] stores length of fib sequence ending at indices i,j
        dp = [[0] * n for _ in range(n)]

        val_to_idx = {num: idx for idx, num in enumerate(arr)}

        for i in range(n):
            for j in range(i):
                # Find if there exists a previous number to form Fibonacci sequence
                diff = arr[i] - arr[j]
                prev_idx = val_to_idx.get(diff, -1)

                # Update dp if valid Fibonacci sequence possible
                # diff < arr[prev] ensures strictly increasing sequence
                dp[j][i] = (
                    dp[prev_idx][j] + 1
                    if diff < arr[j] and prev_idx >= 0
                    else 2
                )
                res = max(res, dp[j][i])

        # Return 0 if no sequence of length > 2 found
        return res if res > 2 else 0