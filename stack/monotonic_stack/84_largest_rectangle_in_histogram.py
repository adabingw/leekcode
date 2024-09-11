class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        res = 0
        nextstack = [-1] * n
        prevstack = [-1] * n
        stack = []

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                nextstack[top] = i
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                prevstack[top] = i
            stack.append(i)
        
        for i in range(n):
            left = prevstack[i]
            right = n if nextstack[i] == -1 else nextstack[i]
            length = right - left - 1
            res = max(res, length * heights[i])
        
        return res