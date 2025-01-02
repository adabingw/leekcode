class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        # when k = n - 1, a valid res is [1, n, 2, n - 1, 3, n - 2]
        # alternating!
        # when k < n - 1, the first n - k elements can have a diff of 1
        # for the remaining, we will have a diff of n - k, n - k - 1...

        res = [i for i in range(1, n - k)]

        for i in range(k + 1):
            if i % 2 == 0:
                res.append(n - k + i // 2)
            else:
                res.append(n - i // 2)
        
        return res