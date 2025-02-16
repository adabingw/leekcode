class Solution(object):
    def maxWeight(self, pizzas):
        """
        :type pizzas: List[int]
        :rtype: int
        """
        pizzas.sort()
        print(pizzas)

        res = 0
        days = len(pizzas) // 4

        for i in range(1, days + 1, 2):
            Z = pizzas.pop()
            res += Z

        for i in range(2, days + 1, 2):
            Z = pizzas.pop()
            Y = pizzas.pop()
            res += Y
            
        return res
        