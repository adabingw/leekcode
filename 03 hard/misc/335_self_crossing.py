class Solution(object):
    def isSelfCrossing(self, distance):
        """
        :type distance: List[int]
        :rtype: bool
        """
        two = three = four = five = 0 
        for one in distance: 
            if four >= two > 0 and (one >= three or one >= three - five >= 0 and six >= four - two): 
                return True 
            two, three, four, five, six = one, two, three, four, five