class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        if target == startFuel: 
            return 0
        
        stations.append([target, 0])
        result = 0
        fuel = startFuel
        pq = []
        miss = []
        position = 0

        for i, s in enumerate(stations):
            distance = s[0] - position
            position = s[0]
            
            if fuel < distance:
                while miss and fuel < distance:
                    fuel += -heapq.heappop(miss)
                    result += 1
                
                if fuel < distance: 
                    return -1
            
            fuel -= distance
            heapq.heappush(miss, -s[1])
        return result
