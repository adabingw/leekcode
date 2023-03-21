from collections import deque 

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        n = len(deck) 
        indices = deque(range(n))
        result = [None] * n 

        # sorted(deck) is the outcome we want 
        # we reverse the reveal process

        for card in sorted(deck): 
            index = indices.popleft() 
            result[index] = card 
            if indices: 
                indices.rotate(-1)

        return result 