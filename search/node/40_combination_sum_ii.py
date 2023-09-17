class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = [] 
        combination = []

        candidates.sort()
        print(candidates)
        def dfs(remain, index):
            if remain == 0: 
                result.append(list(combination))
                return  

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]: 
                    continue 
                
                pick = candidates[i]
                if remain - pick < 0: 
                    break 

                combination.append(pick) 
                dfs(remain - pick, i + 1) 
                combination.pop()


        dfs(target, 0)

        return result
