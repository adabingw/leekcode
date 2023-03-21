class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        answer = []
        for index, price in enumerate(prices): 
            discount = prices[index + 1:] 
            while discount and discount[0] > price: 
                discount.pop(0) 
            if discount: 
                answer.append(price - discount[0]) 
            else: 
                answer.append(price)
        return answer