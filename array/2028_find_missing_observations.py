class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        s = len(rolls) + n
        total = s * mean
        rem = total - sum(rolls)

        if rem <= 0:
            return []

        if rem % n == 0:
            return [rem / n] * n if rem / n <= 6 else []
        else:
            res = [rem // n] * n
            j = 0
            for i in range(rem % n):
                res[j] += 1
                j = (j + 1) % n
            if max(res) > 6 or min(res) < 1:
                return []
            return res
        