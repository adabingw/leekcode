class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (math.factorial(2 * n)/(2 ** n)) % (10 ** 9 + 7)
