class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        
        n = len(prices)
        if n < 2:
            return 0
        
        result = 0
        minimum = prices[0]

        for i in range(1, n):
            if prices[i] < minimum:
                minimum = prices[i]

            # minimum = prices[i] - fee is for if there is a
            # value after prices[i] that is greater than prices[i]
            # that we can use to sell instead of using prices[i]
            # in this case, our new profit would have to add the 
            # difference between prices[new_i] and prices[i]
            # but we need to take into consideration the fee
            # so we "set" minimum to prices[i] - fee so that
            elif prices[i] > minimum + fee:
                result += (prices[i] - fee - minimum)
                minimum = prices[i] - fee
        
        return result
