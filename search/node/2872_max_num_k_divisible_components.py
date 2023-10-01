class Solution(object):
    def maxKDivisibleComponents(self, n, edges, values, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :type k: int
        :rtype: int
        """
        
        # if leaf value % k == 0, separate from tree, comp++
        # if not, part of parent's component -> increase parent's value by leaf value

        if n <= 1:
            return 1
        
        result = 0

        # build adjacency
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        q = []

        # start with the leaves
        for i in graph.keys():
            if len(graph[i]) == 1:
                q.append(i)
        
        # cut leaves layer by layer
        while q:
            n = len(q)
            for _ in range(n):
                u = q.pop()

                # get the parent (if it exists)
                parent = next(iter(graph[u])) if graph[u] else -1

                # if parent exists, we remove u from parent
                if parent != -1:
                    graph[parent].remove(u)
                
                # if u value is divisible by k, detaches
                if values[u] % k == 0:
                    result += 1

                # otherwise, add to parent
                else:
                    if parent != -1:
                        values[parent] += values[u]

                # add parent to q if parent is a leaf now
                if parent != -1 and len(graph[parent]) == 1:
                    q.append(parent)
        
        return result
