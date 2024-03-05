class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        
        special.sort()
        result = special[0] - bottom
        for i in range(0, len(special) - 1):
            result = max(result, special[i + 1] - special[i] - 1)

        result = max(result, top - special[-1])
        return result