class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            l = i + 1
            r = len(nums) - 1
            while r > l:
                if nums[l] + nums[r] + nums[i] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while r > 0 and nums[r] == nums[r - 1]:
                            r -= 1
                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                            l += 1
                    r -= 1
                    l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return result
