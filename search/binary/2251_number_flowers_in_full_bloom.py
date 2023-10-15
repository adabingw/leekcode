class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """

        # number of flowers that started blooming minus
        # number of flowers that finished blooming
        starts = []
        ends = []

        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)

        starts.sort()
        ends.sort()
        result = []

        # bisect_right: returns the right-most index to insert the given 
        # element while maintaining the sorted order.
        for person in people:
            i = bisect_right(starts, person)
            j = bisect_right(ends, person)
            result.append(i - j)
        
        return result
