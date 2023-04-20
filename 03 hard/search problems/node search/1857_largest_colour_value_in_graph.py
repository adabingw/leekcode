class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(colors)

        visited = [False] *  n
        stack = [False] * n
        nodes = defaultdict(list)
        count = [[0] * 26 for _ in range(n)]

        global maximum
        maximum = -1

        for edge in edges: 
            nodes[edge[0]].append(edge[1]) 

        def dfs(node): 
            global maximum 
            if stack[node]: 
                return True
            elif visited[node]: 
                return False 
            
            visited[node] = True 
            stack[node] = True 

            for neighbour in nodes[node]: 
                if dfs(neighbour):
                    return True
                    
                for color in range(26):
                    count[node][color] = max(count[node][color], count[neighbour][color])
            
            curr = ord(colors[node]) - ord('a')
            count[node][curr] += 1 
            maximum = max(maximum, count[node][curr])

            stack[node] = False

            return False

        for i in range(n): 
            if not visited[i]:
                if dfs(i): 
                    return -1 

        return maximum