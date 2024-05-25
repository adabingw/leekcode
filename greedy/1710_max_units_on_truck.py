class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        result = 0
        boxTypes.sort(key=lambda x:-x[1])
        for amount, units in boxTypes:
            if (truckSize - amount < 0):
                result += (truckSize) * units
                truckSize -= amount
                return result
            result += (units * amount)
            truckSize -= amount
        return result