class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        n = len(edges)
        visited = [False] * n 

        global cycle
        cycle = -1 

        def dfs(node, distances): 
            global cycle 
            visited[node] = True 
            neighbour = edges[node] 
            
            if neighbour != -1 and not visited[neighbour]: 
                distances[neighbour] = distances[node] + 1 
                dfs(neighbour, distances)
            elif neighbour != -1 and neighbour in distances: 
                distance = distances[node] - distances[neighbour] + 1 
                cycle = max(cycle, distance)


        for node in range(n): 
            if not visited[node]: 
                distances = defaultdict(int)
                distances[node] = 1 
                dfs(node, distances)

        return cycle 