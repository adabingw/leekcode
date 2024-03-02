class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        rods = defaultdict(set)
        for i in range(0, len(rings) - 1, 2):
            c = rings[i]
            p = rings[i + 1]

            rods[p].add(c)
                
        result = 0
        for k in rods:
            if len(rods[k]) >= 3:
                result += 1
        
        return result