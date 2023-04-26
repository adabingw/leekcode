class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = [[]]

        def dfs(index, path, nums): 
            result.append(path)

            if index == len(nums) - 1: 
                return

            for i, n in enumerate(nums[index + 1:]): 
                dfs(i, path + [n], nums[index + 1:])

        for i, n in enumerate(nums): 
            dfs(i, [n], nums)

        return result