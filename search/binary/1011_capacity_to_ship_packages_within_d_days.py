class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        def fit(w):
            d = 1
            curr_weight = 0
            for weight in weights:
                curr_weight += weight
                if curr_weight > w:
                    d += 1
                    curr_weight = weight
            return d <= days

        lo = max(weights)
        hi = sum(weights)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if fit(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo