class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0 
        left, left_max = 0, 0 
        right, right_max = len(height) - 1, 0
        
        while left < right: 
            if height[left] < height[right]: 
                if height[left] >= left_max: 
                    left_max = height[left]
                else: 
                    area += left_max - height[left]
                left += 1 
            else: 
                if height[right] >= right_max: 
                    right_max = height[right] 
                else: 
                    area += right_max - height[right]
                right -= 1

        return area 