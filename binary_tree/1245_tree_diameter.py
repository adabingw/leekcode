class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = defaultdict(bool)
        adj = defaultdict(list)

        global res
        res = 0
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):

            global res

            # the top 2 distance starting from this node
            top_1_distance, top_2_distance = 0, 0

            distance = 0
            visited[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    distance = 1 + dfs(neighbor)

                if distance > top_1_distance:
                    top_1_distance, top_2_distance = distance, top_1_distance
                elif distance > top_2_distance:
                    top_2_distance = distance

            # with the top 2 distance, we can update the current diameter
            res = max(res, top_1_distance + top_2_distance)

            return top_1_distance

        dfs(0)

        return res
