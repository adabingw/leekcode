class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # sort point by starting x
        points.sort()
        res = 0

        while points:

            if len(points) > 1:
                point = points.pop(0)

                # next balloon does not overlap with current balloon
                if points[0][0] > point[1]:
                    res += 1
                else:

                    # record the min ending x for our interval
                    end = point[1]

                    # while the balloon's starting x is less than end
                    # meaning this balloon can be counted in the interval
                    while points and points[0][0] <= end:
                        # balloon is taken out by arrow
                        p = points.pop(0)
                        end = min(end, p[1])
                    res += 1
            else:
                res += 1
                points.pop()
        return res