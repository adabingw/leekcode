class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        result = 0
        n = len(points)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                distance = manhattan(points[i], points[j])
                graph[i].append((distance, j))
                graph[j].append((distance, i))

        heap = [(0, 0)]
        visited = set()

        while len(visited) < n:
            distance, i = heapq.heappop(heap)
            if i in visited:
                continue
            
            result += distance
            visited.add(i)

            for neighbour_distance, neighbour_i in graph[i]:
                if neighbour_i not in visited:
                    heapq.heappush(heap, (neighbour_distance, neighbour_i))

        return result
