class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        n = len(obstacles)
        result = [1] * n 

        l = []

        for index, obstacle in enumerate(obstacles): 
            i = bisect.bisect_right(l, obstacle) 

            if i == len(l): 
                l.append(obstacle) 
            else: 
                l[i] = obstacle
            
            result[index] = i + 1
        
        return result