class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        n = len(strs)
        adj = defaultdict(list) 
        visited = [False] * n
        count = 0

        def similar(a, b): 
            diff = 0 
            for c in range(len(a)): 
                if a[c] != b[c]: 
                    diff += 1 
            return diff == 0 or diff == 2

        def dfs(node): 
            visited[node] = True 
            for neighbour in adj[node]: 
                if not visited[neighbour]: 
                    dfs(neighbour)

        for i in range(n): 
            for j in range(n): 
                if i != j and similar(strs[i], strs[j]):
                    adj[i].append(j)
                    adj[j].append(i) 
        
        for i in range(n): 
            if not visited[i]: 
                dfs(i)
                count += 1
        
        return count