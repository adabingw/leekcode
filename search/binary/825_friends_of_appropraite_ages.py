class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """

        result = 0
        ages.sort()
        for i in range(len(ages)):
            index = bisect.bisect(ages, ages[i])
            index2 = bisect.bisect(ages, 0.5 * ages[i] + 7)
            result += max(0, index - index2 - 1) 
        return result