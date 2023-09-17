class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        nodes = defaultdict(list)
        for u, v in edges: 
            nodes[u].append(v) 
            nodes[v].append(u)

        pairs = 0 
        component_size = 0 
        remaining_nodes = n

        visited = [False] * n

        def dfs(node): 
            visited[node] = True 
            count = 1 
            for neighbour in nodes[node]: 
                if not visited[neighbour]: 
                    count += dfs(neighbour) 
            return count 
        
        for node in range(n): 
            if not visited[node]: 
                component_size = dfs(node)  
                pairs += component_size * (remaining_nodes - component_size)
                remaining_nodes -= component_size 
        
        return pairs 