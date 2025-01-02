class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels = Counter(jewels)
        res = 0
        for stone in stones:
            res += jewels[stone]

        return res