class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        friends = [i for i in range(1, n + 1)]
        k -= 1
        i = 0 
        while len(friends) > 1: 
            index = (k + i) % len(friends)
            i = index
            friends.pop(index)
        return friends[0]