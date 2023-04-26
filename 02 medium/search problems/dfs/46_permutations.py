class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []

        def dfs(p, nums): 
            
            if not nums: 
                result.append(p) 

            for i, n in enumerate(nums): 
                dfs(p + [n], nums[:i] + nums[i + 1:])

        dfs([], nums) 

        return result        