class Solution(object):
    def minimumCost(self, start, target, specialRoads):
        """
        :type start: List[int]
        :type target: List[int]
        :type specialRoads: List[List[int]]
        :rtype: int
        """
        
        min_heap = [(0, start[0], start[1])] # distance, row, col
        edges = defaultdict(list)

        for x1, y1, x2, y2, cost in specialRoads:
            if abs(x2 - x1) + abs(y2 - y1) < cost:
                continue
            edges[(x1, y1)].append((cost, x2, y2))

        visited = {}

        while min_heap:
            cost, row, col = heappop(min_heap)

            # outdated version, skip it
            if (row, col) in visited:
                continue

            # reached bottom right
            if row == target[0] and col == target[1]:
                return cost

            visited[(row, col)] = cost
            
            # point is at starting point of special road
            if (row, col) in edges:
                for ecost, erow, ecol in edges[(row, col)]:
                    if (erow, ecol) not in visited:
                        heappush(min_heap, (cost + ecost, erow, ecol))
            
            # calculate going directly to starting point of special road
            for r, c in edges:
                if (r, c) not in visited:
                    heappush(min_heap, (cost + abs(row - r) + abs(col - c), r, c))
            
            # calculate going directly to target
            heappush(min_heap, (cost + abs(target[0] - row) + abs(target[1] - col), target[0], target[1]))
