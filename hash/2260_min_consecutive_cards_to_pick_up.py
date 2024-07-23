class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        d = {}
        res = float('inf')
        for index, card in enumerate(cards):
            if card in d:
                res = min(res, index - d[card] + 1)
            d[card] = index
        
        return res if res != float('inf') else -1