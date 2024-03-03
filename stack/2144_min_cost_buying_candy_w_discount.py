class Solution(object):
    def minimumCost(self, costs):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        costs.sort()
        result = 0
        curr = 0

        while costs:
            if curr == 2:
                costs.pop()
                curr = 0
            else:
                curr += 1
                result += costs.pop()
        
        return result