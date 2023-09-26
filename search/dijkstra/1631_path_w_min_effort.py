class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        # path cost is maximum absolute difference in heights 
        # between two diff consecutive cells of the path

        n = len(heights)
        m = len(heights[0])

        distances = [[float('inf')] * m for _ in range(n)]
        distances[0][0] = 0

        min_heap = [(0, 0, 0)] # distance, row, col
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while min_heap:
            distance, row, col = heappop(min_heap)

            # outdated version, skip it
            if distance > distances[row][col]:
                continue

            # reached bottom right
            if row == n - 1 and col == m - 1:
                return distance
            
            for dir in directions:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if 0 <= new_row < n and 0 <= new_col < m:
                    new_distance = max(distance, abs(heights[new_row][new_col] - heights[row][col]))
                    if distances[new_row][new_col] > new_distance:
                        distances[new_row][new_col] = new_distance
                        heappush(min_heap, (distances[new_row][new_col], new_row, new_col))
