class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = [] 
        candidates.sort()

        def dfs(target, index, paths): 
            if target < 0: 
                return 
            if target == 0: 
                res.append(paths) 
            
            print(target, index, paths)
            for i in range(index, len(candidates)):
                dfs(target - candidates[i], i, paths + [candidates[i]])

        dfs(target, 0, []) 

        return res