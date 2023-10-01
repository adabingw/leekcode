class Solution(object):
    def minEdgeReversals(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        g = [[] for _ in range(n)]      # original graph
        rg = [[] for _ in range(n)]     # reversed graph

        for u, v in edges:
            g[u].append(v)
            rg[v].append(u)

        # find find count on node 0
        # every node in our reversed graph increases the count
        def dfs(u, p):
            count = 0
            for v in g[u]:
                if v == p:
                    continue
                count += dfs(v, u)
            for v in rg[u]:
                if v == p:
                    continue
                count += 1
                count += dfs(v, u)
            return count

        result = [0] * n
        result[0] = dfs(0, -1)

        # when we go to a neighbour with directed edge
        # we have to reverse edge to go to parent, count + 1
        # when we go to a neighbour with reverse directed edge
        # we don't need to reverse that edge to go to parent, count - 1
        def dfs2(u, p, count):
            result[u] = count
            for v in g[u]:
                if v == p:
                    continue
                dfs2(v, u, count + 1)
            
            for v in rg[u]:
                if v == p:
                    continue
                dfs2(v, u, count - 1)

        dfs2(0, -1, result[0])
        return result
