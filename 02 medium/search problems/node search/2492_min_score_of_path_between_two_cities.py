class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        visited = set()
        nodes = defaultdict(dict)
        q = deque([1]) 

        minimum = float('inf')

        for roadfrom, roadto, score in roads:
            nodes[roadto][roadfrom] = nodes[roadfrom][roadto] = score
            
        while q: 
            node = q.popleft() 
            for edge, score in nodes[node].items(): 
                minimum = min(minimum, score) 
                if edge not in visited: 
                    visited.add(edge) 
                    q.append(edge)

        return minimum

    def minScore2(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        visited = [] 
        nodes = defaultdict(list)

        global minimum
        minimum = float('inf')

        for road in roads: 
            nodes[road[0]].append([road[1], road[2]]) 
            nodes[road[1]].append([road[0], road[2]])

        def dfs(node): 
            global minimum
            visited.append(node) 
            for edge in nodes[node]: 
                minimum = min(minimum, edge[1]) 
                if edge[0] not in visited: 
                    dfs(edge[0])

        dfs(1)
        return minimum