class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        return sorted(nums, key=lambda x: (d[x], -x))