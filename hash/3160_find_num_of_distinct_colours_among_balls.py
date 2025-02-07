class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
        n = len(queries)
        colours = defaultdict(int)
        balls = defaultdict(int)
        res = []
        curr = 1

        for i in range(n):
            ball, colour = queries[i]
            if balls[ball]:
                # same colour, no change
                prev = balls[ball]
                colours[prev] -= 1

                if colours[prev] == 0:
                    del colours[prev]

            balls[ball] = colour
            colours[colour] += 1

            res.append(len(colours))
        
        return res