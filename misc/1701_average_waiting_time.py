class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        t = -1
        wait = 0
        for arrival, time in customers:
            if t == -1:
                t = arrival + time
                wait = time
            else:
                if arrival > t:
                    t = arrival + time
                    wait += time
                else:
                    t += time
                    wait += t - arrival
        return float(wait) / float(len(customers))