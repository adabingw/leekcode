class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction = sorted(satisfaction)

        max_satisfaction = 0 
        suffix_sum = 0 

        for i in range(len(satisfaction) - 1, -1, -1): 
            if suffix_sum + satisfaction[i] <= 0: 
                continue
            suffix_sum += satisfaction[i] 
            max_satisfaction += suffix_sum 

        return max_satisfaction
