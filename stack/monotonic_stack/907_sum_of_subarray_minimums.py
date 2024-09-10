class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        res = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n or arr[i] <= arr[stack[-1]]):
                j = stack.pop()
                left = stack[-1] if stack else -1
                right = i

                contribution = arr[j] * (right - j) * (j - left)
                res += contribution
            stack.append(i)
    
        return res % (10 ** 9 + 7)
