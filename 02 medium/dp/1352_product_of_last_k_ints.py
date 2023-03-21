class ProductOfNumbers(object):

    def __init__(self):
        self.dp = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        # restart the array because 0 makes everything before it 0
        if num == 0: 
            self.dp = [1]
        else: 
            self.dp.append(self.dp[-1] * num)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        # most likely we restarted the array because of a 0 in the nums
        if k >= len(self.dp): return 0 
        return self.dp[-1] / self.dp[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)