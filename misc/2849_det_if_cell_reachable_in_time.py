class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        height = abs(fy - sy)
        width = abs(fx - sx) 

        if height == 0 or width == 0:
            if height == 0 and width == 0:
                return not t == 1
            if height == 0:
                return width <= t
            if width == 0:
                return height <= t
        
        result = height if height < width else width
        print(result)
        straight = width - result if height < width else height - result
        print(straight)
        result += straight
        return result <= t
