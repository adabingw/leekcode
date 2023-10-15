class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        nums = [i for i in range(1, n + 1)] 
        result = []

        def dfs(index, path, nums): 
            if len(path) == k:
                result.append(path) 
                return

            for i, n in enumerate(nums[index + 1:]): 
                dfs(i, path + [n], nums[index + 1:])

        for i, n in enumerate(nums): 
            dfs(i, [n], nums)

        return result