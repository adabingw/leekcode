class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(key=lambda k: (k[0], -k[1]))

        weak = 0
        max_defense = 0

        for i in range(len(properties) - 1, -1, -1):
            if properties[i][1] < max_defense:
                weak += 1
            
            max_defense = max(max_defense, properties[i][1])
        
        return weak