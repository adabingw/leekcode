class Solution(object):
    def circularGameLosers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        person = 0
        received = []
        num = 1

        while person not in received:
            received.append(person)
            person = (person + num * k) % (n)
            num += 1
        
        losers = []

        for i in range(n):
            if i not in received:
                losers.append(i + 1)
        
        return losers
