class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        global count
        count = 0 
        nodes = defaultdict(list) 

        for u, v in connections: 
            nodes[u].append([v, 1]) 
            nodes[v].append([u, 0])
        
        def dfs(node, parent): 
            global count 
            for child, sign in nodes[node]: 
                if child != parent: 
                    count += sign 
                    dfs(child, node) 

        dfs(0, -1)
        return count