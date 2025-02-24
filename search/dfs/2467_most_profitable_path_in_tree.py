class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        n = len(edges) + 1
        G = [[] for i in range(n)]
        for i,j in edges:
            G[i].append(j)
            G[j].append(i)
        seen = [0] * n

        def dfs(i, d0):
            seen[i] = 1
            res = -float('inf')
            db = 0 if i == bob else n
            for j in G[i]:
                if seen[j]: continue
                cur, kk = dfs(j, d0 + 1)
                res = max(res, cur)
                db = min(db, kk)
            if res == -float('inf'): 
                res = 0
            if d0 == db: 
                res += amount[i] // 2
            if d0 < db: 
                res += amount[i]
            return res, db + 1

        return dfs(0, 0)[0]