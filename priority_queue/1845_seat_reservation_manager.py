class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.seats = [i + 1 for i in range(n)]
        heapq.heapify(self.seats)
        

    def reserve(self):
        """
        :rtype: int
        """
        seat = heapq.heappop(self.seats)
        return seat

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        heapq.heappush(self.seats, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)