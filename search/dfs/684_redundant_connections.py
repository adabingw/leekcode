class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        graph = defaultdict(list)
        visited = set()

        def dfs(i, p):
            if i in visited:
                return True

            visited.add(i)

            for j in graph[i]:
                if j != p and dfs(j, i):
                    return True
            return False

        for u, v in edges:
            visited = set()
            graph[u].append(v)
            graph[v].append(u)

            if dfs(u, -1):
                return [u, v]
        