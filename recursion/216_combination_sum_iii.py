class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n > 45:
            return []
        
        res = []
        
        def rec(k_, n_, i, arr):
            if k_ == 0 and n_ == 0:
                res.append(arr)
                return
            if k_ == 0 or n_ <= 0:
                return
            
            for j in range(i, 10):
                rec(k_ - 1, n_ - j, j + 1, arr + [j])

        rec(k, n, 1, [])
        return res