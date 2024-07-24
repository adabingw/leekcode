class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(nums, key=lambda n: int(''.join(map(lambda d: str(mapping[int(d)]), str(n)))))