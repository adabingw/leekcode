class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        n = len(weights) - 1
        arr = [0] * n
        result = 0
        for i in range(n):
            arr[i] = weights[i] + weights[i + 1]
        print(arr)
        arr.sort()
        # arr.sort(reverse=True)
        print(arr)
        for i in range(k - 1):
            result += (arr[n - 1 - i] - arr[i])
        print(result)
        return result
