class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        min_rank = min(ranks)
        max_rank = max(ranks)

        freq = defaultdict(int)
        for rank in ranks:
            freq[rank] += 1
        
        lo = 1
        hi = min_rank * cars * cars

        while lo < hi:
            mid = (lo + hi) // 2
            num_cars = 0

            for rank in range(1, max_rank + 1):
                num_cars += freq[rank] * int(math.sqrt(mid // rank))

            if num_cars >= cars:
                hi = mid
            else:
                lo = mid + 1
        
        return lo