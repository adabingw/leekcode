class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]

        nums.sort()

        def dfs(index, path, nums): 
            if path not in result:
                result.append(path)

            if index == len(nums) - 1: 
                return

            for i, n in enumerate(nums[index + 1:]): 
                dfs(i, path + [n], nums[index + 1:])

        for i, n in enumerate(nums): 
            dfs(i, [n], nums)

        return result