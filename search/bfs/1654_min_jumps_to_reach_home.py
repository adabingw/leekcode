class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        forbidden = set(forbidden)
        maxForbidden = max(forbidden)
        visited = set()
        visited.add(0)
        queue = deque()
        queue.append((0, 'LEFT'))
        level = 0

        def should_add_to_queue(cur, direction, prev_direction=None):
            return direction != prev_direction and cur >= 0 and cur not in visited and cur not in forbidden and cur <= a + b + max(x, maxForbidden)

        while queue:
            n = len(queue)
            for _ in range(n):
                cur, direction = queue.popleft()
                if cur == x:
                    return level
                after_left, after_right = cur - b, cur + a
                if should_add_to_queue(after_right, 'LEFT'):
                    queue.append((after_right, 'LEFT'))
                    visited.add(after_right)
                if should_add_to_queue(after_left, 'RIGHT', direction):
                    queue.append((after_left, 'RIGHT'))
                    # visited.add(after_left)
            level += 1
        return -1
        