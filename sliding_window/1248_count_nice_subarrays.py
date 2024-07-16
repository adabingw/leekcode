class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # i = 0
        # count = 0
        # res = 0

        # for j in range(len(nums)):
        #     if nums[j] % 2 == 1:
        #         k -= 1
        #         count = 0
        #     while k == 0:
        #         if nums[j] % 2 == 1:
        #             k += 1
        #         i += 1
        #         count += 1
        #     res += count
        # return res

        # alternate:
        # replace even elements with 0 and odd elements with 1
        # number of subarrays with sum k

        for i in xrange(len(nums)):
            nums[i] = nums[i] % 2
        d = defaultdict(int)
        d[0] = 1
        s = 0
        res = 0
        for i in xrange(len(nums)):
            s += nums[i]
            res += d[s - k]
            d[s] += 1
        return res