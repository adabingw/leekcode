class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = defaultdict(list)
        for num in nums:
            num_list = sum([int(i) for i in list(str(num))])
            sums[num_list].append(-num)
        res = -1
        for i in sums:
            if len(sums[i]) >= 2:
                heapify(sums[i])
                n = -heappop(sums[i])
                m = -heappop(sums[i])
                res = max(res, n + m)
        
        return res