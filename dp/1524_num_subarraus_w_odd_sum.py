class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10 ** 9 + 7
        n = len(arr)

        for i in range(n):
            arr[i] = arr[i] % 2

        # dpEven[i] - the number of subarrays ending at index i with an even sum
        # dpOdd[i] - the number of subarrays ending at index i with an odd sum
        dp_even, dp_odd = [0] * n, [0] * n

        # last element even
        if arr[n - 1] == 0:
            dp_even[n - 1] = 1
        # last element odd
        else:
            dp_odd[n - 1] = 1

        for num in range(n - 2, -1, -1):
            if arr[num] == 1:
                dp_odd[num] = (1 + dp_even[num + 1]) % MOD
                dp_even[num] = dp_odd[num + 1]
            else:
                dp_even[num] = (1 + dp_even[num + 1]) % MOD
                dp_odd[num] = dp_odd[num + 1]

        count = 0
        for odd_count in dp_odd:
            count = (count + odd_count) % MOD

        return int(count)