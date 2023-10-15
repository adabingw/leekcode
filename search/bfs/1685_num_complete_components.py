class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        nodes = defaultdict(list)
        result = 0
        components = []
        nums = [i for i in range(n)]

        for u, v in edges:
            nodes[u].append(v)
            nodes[v].append(u)

        while nums:
            q = [nums.pop(0)]
            curr_component = [q[0]]
            while q:
                node = q.pop(0)
                for adj in nodes[node]:
                    if adj not in curr_component:
                        curr_component.append(adj)
                        q.append(adj)
                        if adj in nums:
                            nums.remove(adj)
            components.append(sorted(curr_component))

        for component in components:
            connected = True
            for c in component:
                if sorted(nodes[c] + [c]) != component:
                    connected = False
                    break
            if connected:
                result += 1

        return result
