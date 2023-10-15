class Solution(object):
    def paintWalls(self, cost, time):
        """
        :type cost: List[int]
        :type time: List[int]
        :rtype: int
        """

        # paid paints ith wall, costs cost[i] money, in time[i] time
        # free painter paints time[i] walls
        # we spent cost[i] money to paint 1 + time[i] walls

        n = len(cost)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[n][i] = float('inf')
        
        # remain walls is the remaining number of walls to paint
        # i is the index we're considering
        # for the ith wall, we can either hire paid painter, or not hire them
        #    hire -> spend: cost[i], paint: 1 + time[i] walls   (paint)
        #    don't hire -> spend: 0, paint: 0                   (don't paint)

        # base case: remain <= 0, i == n
        # dp[i][remain] = minimum cost to paint remain walls considering index i and beyond
        # at index i, paint = cost of paint + minimum cost of paint of index i with x remaining walls
        # don't paint = minimum cost of paint of index i with y remaining walls
        # x = remain - (1 + time[i])
        # y = remain
        # we choose the minimum of the two

        for i in range(n - 1, -1, -1):
            for remain in range(1, n):
                paint = cost[i] + dp[i + 1][max(0, remain - 1 - time[i])]
                dont_paint = dp[i + 1][remain]
                dp[i][remain] = min(paint, dont_paint)
        
        return dp[0][n]
