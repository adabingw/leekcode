import copy 

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        global n, paths
        n = len(graph) 
        print(n)
        paths = []

        def dfs(node, path): 
            print(path)
            global n, paths
            if node == n - 1: 
                paths.append(path)
                return
            
            for i in graph[node]: 
                repath = copy.deepcopy(path)
                repath.append(i)
                dfs(i, repath) 
            return 
        
        for i in graph[0]: 
            dfs(i, [0, i])
        return paths
