class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # (prefix[j] - prefix[i]) % k = 0
        # prefix[j] = Q1 * k + R1, prefix[i] = Q2 * k + R2
        # ((Q1 - Q2) * k + (R1 - R2)) % k = 0
        # since (Q1 - Q2) * k is divisible by k,
        # R1 - R2 is also divisible by k
        # both R1 and R2 are in range [0, k).
        # R1 - R2 can be divisible by k if
        # R1 - R2 = 0, or R1 = R2
        # substituting R1 = prefix[j] % k, R2 = prefix[i] % k
        # prefix[j] % k = prefix[i] % k

        prefix_mod = 0
        seen = {0: -1}

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k
            if prefix_mod in seen:
                if i - seen[prefix_mod] > 1:
                    return True
            else:
                seen[prefix_mod] = i
        
        return False