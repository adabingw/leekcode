class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        passengers = 0
        destinations = {}
        trips = sorted(trips, key=lambda x: (x[1], x[2]))
        for trip in trips:
            print(destinations)
            for key in destinations.keys():
                if trip[1] >= key:
                    passengers -= destinations[key]
                    destinations[key] = 0
            passengers += trip[0]
            if trip[2] not in destinations:
                destinations[trip[2]] = 0
            destinations[trip[2]] += trip[0]
            if passengers > capacity:
                return False
        return True 
