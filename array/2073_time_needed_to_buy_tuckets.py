class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time = 0 
        for i, t in enumerate(tickets): 
            if i <= k: 
                time += min(t, tickets[k])
            else: 
                time += min(t, tickets[k] - 1)
        return time 