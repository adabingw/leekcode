class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        current = 0
        stack = []

        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = current - stack[-1] - 1
                bounded = min(height[current], height[stack[-1]]) - height[top]
                res += distance * bounded
            stack.append(current)
            current += 1
        return res
