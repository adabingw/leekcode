class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        friends = [[times[i][0], times[i][1], i] for i in range(len(times))]
        friends.sort()

        # stores available seats
        seats = [i for i in range(len(friends))]

        # stores leave time, which seat they sat at
        occupied = []
        for i, j, f in friends:
            while occupied and occupied[0][0] <= i:
                t, s = heappop(occupied)
                heappush(seats, s)
            
            # occupy smallest seat
            seat = heappop(seats)
            if f == targetFriend:
                return seat

            heappush(occupied, (j, seat))