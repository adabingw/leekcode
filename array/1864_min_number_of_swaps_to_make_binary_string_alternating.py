class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = [int(item) for item in s]
        n = len(s)
        cul = sum(s)

        if n % 2 and (cul != n // 2 and cul != n // 2 + 1):
            return -1
        elif not n % 2 and cul != n // 2:
            return -1

        miss_0 = 0
        miss_1 = 0

        for i in range(0, n, 2):
            miss_0 += s[i] != 0
            miss_1 += s[i] != 1
        
        return min(miss_0, miss_1) if cul == n - cul else miss_0 if n - cul > cul else miss_1