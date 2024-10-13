class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_mod = 0
        seen = defaultdict(int)
        seen[0] += 1
        res = 0
        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i] % k + k) % k
            res += seen[prefix_mod]
            seen[prefix_mod] += 1
        
        return res