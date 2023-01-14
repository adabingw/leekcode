class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy = 0 
        sell = 1 #Sell
        max_profit = 0
        while sell < len(prices):
            curr = prices[sell] - prices[buy] #our current Profit
            if prices[buy] < prices[sell]:
                max_profit = max(curr, max_profit)
            else:
                buy = sell
            sell += 1
        return max_profit
            