class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1 
        
        nodes = defaultdict(list) 
        for x, y in connections: 
            nodes[x].append(y) 
            nodes[y].append(x) 
        
        visited = [False] * n
        connected = 0 

        def dfs(node): 
            visited[node] = True
            for neighbours in nodes[node]: 
                if not visited[neighbours]:
                    dfs(neighbours) 

        for node in range(n): 
            if not visited[node]:
                connected += 1
                dfs(node) 
        
        return connected - 1