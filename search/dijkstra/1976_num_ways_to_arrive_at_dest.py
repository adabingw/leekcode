class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
        adj = defaultdict(list)
        MOD = 10**9 + 7
        for u, v, t in roads:
            adj[u].append([v, t])
            adj[v].append([u, t])
        
        dist = [float('inf')] * n
        dist[0] = 0
        
        count = [0] * n
        count[0] = 1
        
        heap = [(0, 0)]

        while heap:
            (min_d, i) = heappop(heap)
            if i == n - 1:
                return count[i] % MOD
            
            for neighbour, time in adj[i]:
                t = min_d + time

                if t == dist[neighbour]:
                    count[neighbour] += count[i]
                
                elif t < dist[neighbour]:
                    dist[neighbour] = t
                    heappush(heap, (t, neighbour))
                    count[neighbour] = count[i]