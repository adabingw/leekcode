class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj = {}
        max_rank = 0
        for road in roads:
            if road[0] not in adj:
                adj[road[0]] = []
            if road[1] not in adj:
                adj[road[1]] = []
            
            adj[road[0]].append(road[1])
            adj[road[1]].append(road[0])
        for adj1 in adj:
            for adj2 in adj:
                if adj1 == adj2:
                    continue
                
                rank = len(adj[adj1]) + len(adj[adj2])
                if adj2 in adj[adj1]:
                    rank -= 1

                max_rank = max(max_rank, rank)

        return max_rank    
