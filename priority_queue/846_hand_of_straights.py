class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False

        card_count = Counter(hand)

        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            card = min_heap[0]
            for i in range(groupSize):

                if card_count[card + i] == 0:
                    return False
                    
                card_count[card + i] -= 1
                if card_count[card + i] == 0:
                    if card + i != heapq.heappop(min_heap):
                        return False
        
        return True