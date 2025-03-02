class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        d = defaultdict(int)

        # Copying the array nums1 to the map.
        for nums in nums1:
            d[nums[0]] = nums[1]

        # Adding the values to existing keys or create new entries.
        for nums in nums2:
            d[nums[0]] = d[nums[0]] + nums[1]

        res = []
        for i, v in sorted(d.items()):
            res.append([i, v])

        return res