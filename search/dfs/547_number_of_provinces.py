class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(i):
            for neighbour in adj[i]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    dfs(neighbour)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    adj[i].append(j)
                    adj[j].append(i)
        
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                provinces += 1
                dfs(i)

        return provinces